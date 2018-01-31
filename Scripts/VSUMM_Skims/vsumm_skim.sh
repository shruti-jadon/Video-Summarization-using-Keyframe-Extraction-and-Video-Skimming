#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM_Skims/;
HOMEDIR=$PWD;
# choose pre-sampling rates and number of clusters for videos
# -1 for percent defaults to 1/100 of video length

# sampling rates for future use
# "1" "2" "5" "10" "25" "30"

# percent of the actual video
for percent in "15"; do
	for sampling_rate in "5"; do
		for filename in $DIR*".mp4"; do
			echo $filename
			cd $HOMEDIR
			name=${filename##*/};
			folder_name=${name%.mp4};
			mkdir $OUT$folder_name;
			# mkdir $OUT$folder_name"/keyframes";
			python vsumm_skim.py $filename $sampling_rate $percent $OUT$folder_name"/" color_hist;
			cd ../Evaluation
			python evaluate.py $filename $sampling_rate $percent $OUT$folder_name"/" $OUT$folder_name"/final_results_color_hist_"$percent".txt" color_hist 1;
		done
	done
done