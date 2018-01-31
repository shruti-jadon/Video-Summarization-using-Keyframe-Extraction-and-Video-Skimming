#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/Uniform_Sampling/;
HOMEDIR=$PWD;
sampling_rate="1";

for percent in "15"; do
	echo $percent
	for filename in $DIR*".mp4";do
		echo $filename
		cd $HOMEDIR
		name=${filename##*/};
		folder_name=${name%.mp4};
		echo "printing previous shit"
		echo $folder_name
		mkdir $OUT$folder_name;
		echo $OUT$folder_name
		python uniform.py $filename $percent $OUT$folder_name"/";
		cd ../Evaluation
		pwd 
		echo "printing the stuff"
		echo $filename
		echo $sampling_rate
		echo $percent
		echo $OUT$folder_name"/" $OUT$folder_name"/final_results_uniform_"$percent".txt"
		python evaluate.py $filename $sampling_rate $percent $OUT$folder_name"/" $OUT$folder_name"/final_results_uniform_"$percent".txt" uniform;
	done
done