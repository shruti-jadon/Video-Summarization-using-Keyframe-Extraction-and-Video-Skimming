#!/bin/bash
pwd=dir/
name=$1;
folder_name=${name%.mp4};
allFrames=allFrames;
keyFrames=keyFrames;
rm -r $folder_name"/"
mkdir $folder_name
cd $folder_name		#pwd=dir/$folder_name
mkdir $allFrames
cd $allFrames		#pwd=dir/$folder_name/$allFrames
ffmpeg -i ../../../../Data/SumMe/videos/$name image%d.jpg
mkdir ../$keyFrames
cd ../../			#pwd=dir/
python videoSumSIFT.py ../../Data/SumMe/videos/$name $folder_name
# cd $folder_name/$keyFrames/		#pwd=dir/$folder_name/$keyFrames
# ffmpeg -i image%d.jpg ../summary_modified.mp4