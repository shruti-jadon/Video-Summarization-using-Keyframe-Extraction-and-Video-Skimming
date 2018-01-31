import sys
sys.path.append("/home/shibhansh/ml/cs771/VideoSummarization/Data/python")
import os
from summe import *
import imageio
# System Arguments
# Argument 1: Location of the video
# Argument 2: Location of predicted summary
# Argument 3: Location to store results : typically of the form 'result_"video_name".txt'

def main():
	video=sys.argv[1]
	video_name = sys.argv[1]
	video_name = video_name.split('/')
	video_name = video_name[-1].split('.')[0]
	print "video_name ", video_name
	directory=sys.argv[2]

	print "Getting frames of summary!"
	frame_indices=[int(idx) for idx in open(directory+'/frame_indices_'+video_name+'.txt','r').read().splitlines()]
	print "Got the frames'"

	video=video.split('/')
	videoName=video[len(video)-1].split('.')[0]
	print videoName
	
	video[len(video)-2]="GT"
	HOMEDATA='/'.join(video[0:len(video)-1])
	print HOMEDATA
	
	f_measure, summary_length=evaluateSummary(frame_indices,videoName,HOMEDATA)
	print "F-measure %.3f at length %.2f" %(f_measure, summary_length)

	out_file=open(sys.argv[3],'a')
	out_file.write("F-measure, Summary Length\n")
	out_file.write("%f,%f\n"%(f_measure,summary_length))

if __name__ == '__main__':
	main()