# imgtov
Imgtov (**im**a**g**es **to** **v**ideo converter) creates a video file from a set of images, audio file and text file describing when and what image to display.

### Installation ###

The tool uses ffmpeg and imagemagick:

```sudo apt-get install ffmpeg imagemagick```

### How to run ### 

Put your timestamps in input.txt (format below). Set the desired image_size for conversion, which sets the quality of the video, and audio_track file name. Put the image files in the images directory. Put the audio file in the root. Run imgtov.py. As a result, you should get video.mp4.

input.txt example: 

```ignorelang
# image_size="2560X1440" # 1920X1080, 2560X1440, 3840X2160, 7680X4320
# audio_track="input.mp3"
# 00:00:00.000|Screen Shot 2022-10-29 at 00.41.17.png|Intro
image_size="2560X1440"
audio_track="input.mp3"
00:00:00.000|Screen Shot 2022-10-29 at 00.41.17.png|Intro
00:00:12.673|Screen Shot 2022-10-29 at 00.41.43.png|Vulristics
00:00:17.578|Screen Shot 2022-10-29 at 00.42.00.png|All vulnerabilities  - show generation
00:00:21.839|Screen Shot 2022-10-29 at 00.42.15.png|Vulnerability statistics
00:00:28.362|Screen Shot 2022-10-29 at 00.43.11.png|RCE Exchange blog
00:00:35.737|Screen Shot 2022-10-29 at 00.44.34.png|RCE Exchange First RCE report
00:00:40.379|Screen Shot 2022-10-29 at 00.44.22.png|RCE Exchange Second RCE report
00:00:44.583|Screen Shot 2022-10-29 at 00.43.11.png|RCE Exchange blog
00:01:04.090|Screen Shot 2022-10-29 at 00.45.13.png|RCE Exchange Microsoft
00:01:18.201|Screen Shot 2022-10-29 at 00.43.11.png|RCE Exchange blog
00:01:26.136|Screen Shot 2022-10-29 at 00.45.48.png|RCE Exchange Patches
00:01:39.581|Screen Shot 2022-10-29 at 00.46.04.png|Windows COM+ blog
00:01:49.164|Screen Shot 2022-10-29 at 00.46.22.png|Windows COM+ report
00:02:02.793|Screen Shot 2022-10-29 at 00.46.04.png|Windows COM+ blog
00:02:33.099|Screen Shot 2022-10-29 at 00.47.00.png|3 exploits blog
00:03:01.995|Screen Shot 2022-10-29 at 00.47.18.png|3 exploits report (1)
00:03:10.640|Screen Shot 2022-10-29 at 00.47.33.png|3 exploits report (2)
00:03:19.311|Screen Shot 2022-10-29 at 00.48.00.png|3 exploits report (3)
00:03:26.380|Screen Shot 2022-10-29 at 00.48.19.png|EoP AD blog
00:03:34.508|Screen Shot 2022-10-29 at 00.48.33.png|EoP AD report
00:03:52.421|Screen Shot 2022-10-29 at 00.48.19.png|EoP AD blog
00:04:03.010|Screen Shot 2022-10-29 at 00.48.46.png|Azure blog
00:04:13.723|Screen Shot 2022-10-29 at 00.49.25.png|Azure report
00:04:30.067|Screen Shot 2022-10-29 at 00.48.46.png|Azure blog
00:04:43.197|Screen Shot 2022-10-29 at 00.49.46.png|Office blog
00:04:50.826|Screen Shot 2022-10-29 at 00.50.23.png|Office report
00:05:03.982|Screen Shot 2022-10-29 at 00.49.46.png|Office blog
00:05:39.990|Screen Shot 2022-10-29 at 00.49.46.png|END
```

imgtov.py output example: 

```ignorelang
Getting prameters from input.txt...
image_size: 2560X1440
audio_track: input.mp3
Getting timestamps and filenames from input.txt...
Checking that all files exist in images directory...
1/21. images/Screen Shot 2022-10-29 at 00.41.17.png - file exists
2/21. images/Screen Shot 2022-10-29 at 00.41.43.png - file exists
3/21. images/Screen Shot 2022-10-29 at 00.42.00.png - file exists
4/21. images/Screen Shot 2022-10-29 at 00.42.15.png - file exists
5/21. images/Screen Shot 2022-10-29 at 00.43.11.png - file exists
6/21. images/Screen Shot 2022-10-29 at 00.44.22.png - file exists
7/21. images/Screen Shot 2022-10-29 at 00.44.34.png - file exists
8/21. images/Screen Shot 2022-10-29 at 00.45.13.png - file exists
9/21. images/Screen Shot 2022-10-29 at 00.45.48.png - file exists
10/21. images/Screen Shot 2022-10-29 at 00.46.04.png - file exists
11/21. images/Screen Shot 2022-10-29 at 00.46.22.png - file exists
12/21. images/Screen Shot 2022-10-29 at 00.47.00.png - file exists
13/21. images/Screen Shot 2022-10-29 at 00.47.18.png - file exists
14/21. images/Screen Shot 2022-10-29 at 00.47.33.png - file exists
15/21. images/Screen Shot 2022-10-29 at 00.48.00.png - file exists
16/21. images/Screen Shot 2022-10-29 at 00.48.19.png - file exists
17/21. images/Screen Shot 2022-10-29 at 00.48.33.png - file exists
18/21. images/Screen Shot 2022-10-29 at 00.48.46.png - file exists
19/21. images/Screen Shot 2022-10-29 at 00.49.25.png - file exists
20/21. images/Screen Shot 2022-10-29 at 00.49.46.png - file exists
21/21. images/Screen Shot 2022-10-29 at 00.50.23.png - file exists
Preparing files in processed_images directory...
1/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.41.17.png - file exists
2/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.41.43.png - file exists
3/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.42.00.png - file exists
4/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.42.15.png - file exists
5/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.43.11.png - file exists
6/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.44.22.png - file exists
7/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.44.34.png - file exists
8/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.45.13.png - file exists
9/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.45.48.png - file exists
10/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.46.04.png - file exists
11/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.46.22.png - file exists
12/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.47.00.png - file exists
13/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.47.18.png - file exists
14/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.47.33.png - file exists
15/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.48.00.png - file exists
16/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.48.19.png - file exists
17/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.48.33.png - file exists
18/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.48.46.png - file exists
19/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.49.25.png - file exists
20/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.49.46.png - file exists
21/21. processed_images/2560X1440_Screen Shot 2022-10-29 at 00.50.23.png - file exists
Preparing ffmpeg_input...
Making video...
video.mp4 created!
```

Video example: https://www.youtube.com/watch?v=NJmLgAjyxmE