import re
import subprocess


def execute_command(command):
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    return output.decode('utf-8')


def get_millisecnds(ts_line):
    ms = (int(ts_line.split(":")[0])*60*60 + int(ts_line.split(":")[1])*60
          + int(ts_line.split(":")[2].split(".")[0])) * 1000 + int(ts_line.split(":")[2].split(".")[1])
    return (ms)

'''
#ls Images/ | xargs -i  convert -resize 7680X4320 -background black -gravity center -extent 7680X4320  Images/'{}' ResizedImages/'{}'
ffmpeg -f concat -safe 0 -i input.txt -c copy MergedFile.mp4

ffmpeg -i MergedFile.mp4 -i video.mp3 -map 0:v -map 1:a -c:v copy -shortest output.mp4

'''

def get_config():
    f = open("input.txt", "r")
    config = f.read()
    f.close()
    return config

def remove_comments_from_config(config):
    lines = list()
    for line in config.split("\n"):
        line = re.sub("#.*","",line)
        line = re.sub("[ \t]*$", "", line)
        if line != "":
            lines.append(line)
    return "\n".join(lines)

def get_image_size(config):
    image_size = None
    for line in config.split("\n"):
        if "=" in line:
            if line.split("=")[0] == "image_size":
                image_size = line.split("=")[1].split("\"")[1]
    return image_size

def get_audio_track(config):
    audio_track = None
    for line in config.split("\n"):
        if "=" in line:
            if line.split("=")[0] == "audio_track":
                audio_track = line.split("=")[1].split("\"")[1]
    return audio_track

def get_ts_list(config):
    ts_list = list()
    for line in config.split("\n"):
        if "|" in line:
            ts_list.append(line)
    return ts_list

def get_raw_images_set(ts_list):
    raw_images = set()
    for line in ts_list:
        raw_images.add(line.split("|")[1])
    return raw_images


from pathlib import Path


def check_raw_images_exist(raw_images_set, dir_name):
    raw_images_list = list(raw_images_set)
    raw_images_list.sort()
    n = 0
    for file_name in raw_images_list:
        n += 1
        my_file = Path(dir_name + "/" + file_name)
        if my_file.is_file():
            print(str(n) + "/" + str(len(raw_images_list))+ ". " + dir_name + "/" + file_name + " - file exists")
        else:
            print(str(n) + "/" + str(len(raw_images_list))+ ". " + dir_name + "/" + file_name + " - file does NOT exist")
            print("Error! Exiting...")
            exit()


def check_create_processed_images(raw_images_set, raw_dir_name, processed_dir_name, image_size):
    raw_images_list = list(raw_images_set)
    raw_images_list.sort()
    n = 0
    for file_name in raw_images_list:
        n += 1
        raw_file_path = raw_dir_name + "/" + file_name
        processed_file_path = processed_dir_name + "/" + image_size + "_" + file_name

        my_file = Path(processed_file_path)
        if my_file.is_file():
            print(str(n) + "/" + str(len(raw_images_list))+ ". " + processed_file_path + " - file exists")
        else:
            print(str(n) + "/" + str(len(raw_images_list))+ ". " + processed_file_path + " - file does NOT exist")
            print("Creating...")

            command = "convert -resize " + image_size + " -background black -gravity center -extent " + image_size + " '" + \
              raw_file_path + "' '" + processed_file_path + "'"
            print(command)
            print("Created!")

            execute_command(command)


def get_ffmpeg_input(config, image_size):
    result = list()
    last_img = ""
    last_ts_line = ""

    lines = list()
    for line in config.split("\n"):
        if "|" in line:
            lines.append(line)
    if len(lines) == 0:
        print("Error: timestamps are not set!")
        exit()
    lines.append(lines[len(lines)-1])
    for line in lines:
        if last_img != "":
            ts_line = line.split("|")[0]
            duration = get_millisecnds(ts_line) - get_millisecnds(last_ts_line)
            result.append("file processed_images/" + image_size + "_" + re.sub(" ","\ ", last_img))
            result.append("duration " + str(duration) + "ms")
        last_img = line.split("|")[1]
        last_ts_line = line.split("|")[0]
    result.append("\n")
    return "\n".join(result)

def make_video(ffmpeg_input, audio_track):
    f = open("ffmpeg_input.txt","w")
    f.write(ffmpeg_input)
    f.close()
    command = "ffmpeg -f concat -safe 0 -i ffmpeg_input.txt -c copy video_without_audio.mp4"
    execute_command(command)
    command = "rm video.mp4; ffmpeg -i video_without_audio.mp4 -i " + audio_track + \
              " -map 0:v -map 1:a -c:v copy -shortest video.mp4; rm video_without_audio.mp4; rm ffmpeg_input.txt"
    execute_command(command)


print("Getting prameters from input.txt...")
config = get_config()
config = remove_comments_from_config(config)
image_size = get_image_size(config)
if not image_size:
    print("Error: image_size is not set!")
    exit()
audio_track = get_audio_track(config)
if not image_size:
    print("Error: audio_track is not set!")
    exit()
print("image_size: " + image_size)
print("audio_track: " + audio_track)

print("Getting timestamps and filenames from input.txt...")
ts_list = get_ts_list(config)
raw_images_set = get_raw_images_set(ts_list)

print("Checking that all files exist in images directory...")
raw_dir_name = "images"
check_raw_images_exist(raw_images_set, raw_dir_name)

print("Preparing files in processed_images directory...")
processed_dir_name = "processed_images"
check_create_processed_images(raw_images_set, raw_dir_name, processed_dir_name, image_size)

print("Preparing ffmpeg_input...")
ffmpeg_input = get_ffmpeg_input(config, image_size)

print("Making video...")
make_video(ffmpeg_input, audio_track)
print("video.mp4 created!")
