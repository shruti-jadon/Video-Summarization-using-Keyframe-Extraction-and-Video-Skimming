import sys
import cv2
import os
# System Arguments
# Argument 1: Location of the video
# Argument 2: Percent of summary required
# Argument 3: Directory where indices will be saved

#percent of video for summary 
percent=int(sys.argv[2])

def main():
	global percent
	print "Opening Video!"
	capture=cv2.VideoCapture(os.path.abspath(os.path.expanduser(sys.argv[1])))
	print "Video opened\nGenerating uniformly sampled summary"
	frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
	print frame_count
	sampling_rate=100/percent
	if 100%percent:
		sampling_rate=sampling_rate+1
	frame_indices=[i for i in range(frame_count) if i%sampling_rate==0]

	print "Saving frame indices"
	out_file=open(sys.argv[3]+"frame_indices_uniform_"+str(percent*frame_count/100)+"_1.txt",'w')
	for idx in frame_indices:
		out_file.write(str(idx)+'\n')
	print "Saved indices"

if __name__ == '__main__':
	main()