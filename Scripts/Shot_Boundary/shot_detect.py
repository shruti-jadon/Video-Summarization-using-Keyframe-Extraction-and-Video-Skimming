#!/usr/bin/python
"""
Usage:
Put shot_detect.py and input.avi (input avi file) in the same folder and execute shot_detect.py

Output:
a scene/ subfolder containing clips, 
each taken as a scene
"""

import os, sys, glob

# Get duration of the video file
if os.path.exists('duration.txt'):
    os.remove('duration.txt')

cmd = 'ffmpeg -i input.avi 2>&1|grep "Duration">> duration.txt'
os.system(cmd)

print ' ================= '
print 'Detecting shot boundaries...'
print ' ================= '
if os.path.exists('scenes.txt'):
	os.remove('scenes.txt')

cmd = 'ffprobe -show_frames -of compact=p=0 -f lavfi "movie=input.avi,select=gt(scene\,0.3)">> scenes.txt'
os.system(cmd)


# uncompress the movie file for accurate partition
# skip this if you do not need high accuracy
print ' ================= '
print 'computing raw video for accurate segmentation...'
print ' ================= '
cmd = 'ffmpeg -i input.avi -vcodec rawvideo -acodec copy uncompressed.avi' #pcm_s16le
os.system(cmd)

# read time stamps for keyframes
print ' ================= '
print 'Partitioning video...'
print ' ================= '
seginfo = 'scenes.txt'
if not os.path.exists('scenes'):
	os.mkdir('scenes')

tb = '0'
te = '0'
count = 1
f = open('scenesFinal.txt', 'w')
for line in open(seginfo,'r'):
    line = line.replace("|"," ")
    line = line.replace("="," ")
    parts = line.split()
    te = parts[11] # timestamp
    te = float(te)
    fstr = str(count) + ' ' + str(te) + '\n'
    f.write(fstr)
    cmd = 'ffmpeg -ss '
    tb = float(tb)
    # start time
    if (count == 1):
        tbw = '00:00:00' # first shot
    else:
        tbh = int(tb/3600)
        tbm = int((tb%3600)/60)
        tbs = ((tb%3600)%60)%60
        tbw = str(tbh) + ':' + str(tbm) + ':' + str(tbs)
    cmd += tbw + ' -i uncompressed.avi -vcodec mpeg4 -acodec copy -t ' # change codecs if necessary
    # duration
    td = te - tb
    tdh = int(td/3600)
    tdm = int((td%3600)/60)
    tds = ((td%3600)%60)%60
    tdw = str(tdh) + ':' + str(tdm) + ':' + str(tds)
    cmd += tdw + ' scenes/' + '%(#)04d.avi' % {"#":count}
    os.system(cmd)
    tb = te
    count += 1

# last shot
# cmd = 'ffmpeg -ss '
# tbh = int(tb/3600)
# tbm = int((tb%3600)/60)
# tbs = ((tb%3600)%60)%60
# tbw = str(tbh) + ':' + str(tbm) + ':' + str(tbs)
# cmd += tbw + ' -i uncompressed.avi -vcodec mpeg4 -acodec copy -t ' # change codecs if necessary

# dur = 'duration.txt';
# for line in open(dur,'r'):
#     line = line.replace(":"," ")
#     line = line.replace(","," ")
#     parts = line.split()
#     te = float(parts[1])*3600 + float(parts[2])*60 + float(parts[3])

# td = te-tb
# tdh = int(td/3600)
# tdm = int((td%3600)/60)
# tds = int(((td%3600)%60)%60)
# tds = ((td%3600)%60)%60
# tdw = str(tdh) + ':' + str(tdm) + ':' + str(tds)
# cmd += tdw + ' scenes/' + '%(#)04d.avi' % {"#":count}
# os.system(cmd)
# fstr = str(count) + ' ' + str(te) + '\n'
# f.write(fstr)

os.remove('scenes.txt')
os.remove('uncompressed.avi')
