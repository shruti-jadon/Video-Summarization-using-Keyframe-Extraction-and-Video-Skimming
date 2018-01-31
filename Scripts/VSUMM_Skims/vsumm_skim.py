import sys
sys.path.append("../VSUMM")
import os
import scipy.io
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from get_video_feat import *

# System Arguments
# Argument 1: Location of the video
# Argument 2: Sampling rate (every kth frame is chosen)
# Argument 3: Percentage length of video summary
# Argument 4: Directory where frame indices will be saved
# Argument 5: Name of the features used

# frame chosen every k frames
sampling_rate=int(sys.argv[2])

# percentage of video for summary
percent=int(sys.argv[3])

# skim length per chosen frames in second
# which will be adjusted according to the fps of the video
skim_length=1.8

def main():
	global sampling_rate, percent, skim_length
	print "Opening Video!"
	video=cv2.VideoCapture(os.path.abspath(os.path.expanduser(sys.argv[1])))
	print "Video opened\nChoosing frames"
	
	fps=int(video.get(cv2.CAP_PROP_FPS))
	frame_count=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
	skim_frames_length=fps*skim_length
	
	frames = []
	i=0
	while(video.isOpened()):
		if i%sampling_rate==0:
			video.set(1,i)
			# print i
			ret, frame = video.read()
			if frame is None :
				break
			#im = np.expand_dims(im, axis=0) #convert to (1, width, height, depth)
			# print frame.shape
			frames.append(np.asarray(frame))
		i+=1
	frames = np.array(frames)#convert to (num_frames, width, height, depth)
	
	print "Frames chosen"
	print "Length of video %d" % frames.shape[0]
	
	# REPLACE WITH APPROPRIATE FEATURES
	features=get_color_hist(frames,16)
	print "Shape of features: " + str(features.shape)

	# clustering: defaults to using the features
	print "Clustering"

	# Choosing number of centers for clustering
	num_centroids=int(percent*frame_count/skim_frames_length/100)+1
	print "Number of clusters: "+str(num_centroids)

	#kmeans=KMeans(n_clusters=num_centroids).fit(features)
	kmeans=GaussianMixture(n_components=num_centroids).fit(features)
	print "Done Clustering!"
	
	centres=[]
	features_transform=kmeans.transform(features)
	for cluster in range(features_transform.shape[1]):
		centres.append(np.argmin(features_transform.T[cluster]))

	centres=sorted(centres)
	frames_indices=[]
	for centre in centres:
		print centre
		for idx in range(max(int(centre*sampling_rate-skim_frames_length/2),0),min(int(centre*sampling_rate+skim_frames_length/2)+1,frame_count)):
			frames_indices.append(idx)
	frames_indices=sorted(set(frames_indices))

	print "Saving frame indices"
	out_file=open(sys.argv[4]+"frame_indices_"+sys.argv[5]+'_'+str(num_centroids)+"_"+str(sampling_rate)+".txt",'w')
	for idx in frames_indices:
		out_file.write(str(idx)+'\n')
	print "Saved indices"

if __name__ == '__main__':
	main()