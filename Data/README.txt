############################
#                          #
# THE SUMME BENCHMARK      #
#                          #
############################

 Dataset & evaluation code of the paper 
	Creating Summaries from User Videos
	by Michael Gygli, Helmut Grabner, Hayko Riemenschneider and Luc Van Gool
	published in ECCV 2014, Zurich.

 Code by Michael Gygli, PhD student @ ETH Zurich, Switzerland
 Version: 0.1

 Please report problems regarding the standard evaluation procedure to gygli@vision.ee.ethz.ch

==========
CONTAINS:

 demo.m 		File that shows how to evaluate your summary from matlab

 GT/			folder containing the human summary selections
			each file contins information about the video (length, FPS) and
			- the individual summaries per user (user_score and segments)
			- the averaged score: selections/views (gt_score)

 videos/		folder with the videos themselves in webm format

 matlab/		code for the evaluation including plotting

 python/		basic code for evaluating in python (needs scipy, numpy, matplotlib)
			to run the python demo call (from the dataset root): 
				python python/demo.py

==========
LICENCE: 

The videos were partially downloaded from YouTube and may subject to copyright. We don't own the copyright of the videos and only provide them for non-commercial research purposes only.
The annotation data can be used freely for research purposes. Please cite:

@inproceedings{GygliECCV14,
   author ={Gygli, Michael and Grabner, Helmut and Riemenschneider, Hayko and Van Gool, Luc},
   title = {{Creating Summaries from User Videos}},
   booktitle = {ECCV},
   year = {2014}
}
