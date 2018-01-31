#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM/;
HOMEDIR=$PWD;
# choose pre-sampling rates and number of clusters for videos
# -1 for percent defaults to 1/100 of video length

# sampling rates for future use
# "1" "2" "5" "10" "25" "30"

# percent of the actual video
for percent in "15"; do
	for sampling_rate in "5"; do
		for filename in $DIR"playing_ball.mp4"; do
			echo "parameters for vsumm feat"
			echo $filename
			echo $sampling_rate
			cd $HOMEDIR
			name=${filename##*/};
			folder_name=${name%.mp4};
			mkdir $OUT$folder_name;
			# mkdir $OUT$folder_name"/keyframes";
			echo $percent
			echo $$OUT$folder_name"/"

			echo "parameters for evaluation"
			echo $filename
			echo $sampling_rate
			echo $percent
			echo $OUT$folder_name"/" $OUT$folder_name"/Final_Results_cnn_reduced_"$percent".txt"
			python vsumm_feat.py $filename $sampling_rate $percent 0 0 1 $OUT$folder_name"/" cnn_reduced;
			cd ../Evaluation
			
			python evaluate.py $filename $sampling_rate $percent $OUT$folder_name"/" $OUT$folder_name"/Final_Results_cnn_reduced_"$percent".txt" cnn_reduced;
		done
	done
done