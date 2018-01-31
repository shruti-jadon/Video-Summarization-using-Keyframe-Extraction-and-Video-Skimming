# generic VSUMM to test with different features
# k means clustering to generate video summary
import sys

import numpy as np
import cv2
import scipy.io
import os

# k-means
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from get_video_feat import *

# System Arguments
# Argument 1: Location of the video
# Argument 2: Sampling rate (k where every kth frame is chosed)
# Argument 3: Percentage of frames in the keyframe summany (Hence the number of cluster)
# NOTE: pass the number of clusters as -1 to choose 1/50 the number of frames in original video
# Only valid for SumMe dataset

# optional arguments 
# Argument 4: 1: if 3D Histograms need to be generated and clustered, else 0
# Argument 5: 1: if want to save keyframes 
# Argument 6: 1: if want to save the frame indices
# Argument 7: directory where keyframes will be saved
# Argument 8: Name of the features used

# frame chosen every k frames
sampling_rate=int(sys.argv[2])

# percent of video for summary
percent=int(sys.argv[3])

# globalizing
num_centroids=0

def save_keyframes(frame_indices, summary_frames):
	global sampling_rate, num_centroids
	if int(sys.argv[6])==1:
		print ("Saving frame indices")
		out_file=open(sys.argv[7]+"frame_indices_"+sys.argv[8]+'_'+str(num_centroids)+"_"+str(sampling_rate)+".txt",'w')
		for idx in frame_indices:
			out_file.write(str(idx*sampling_rate)+'\n')
		print ("Saved indices")

	if int(sys.argv[5])==1:
            print ("Saving frames")
            for i,frame in enumerate(summary_frames):
                cv2.imwrite(str(sys.argv[7])+"keyframes/frame%d.jpg"%i, frame)
            print ("Frames saved")

def main():
    global num_bins, sampling_rate, num_centroids, percent
    print ("Opening video!")
    capture = cv2.VideoCapture(os.path.abspath(os.path.expanduser(sys.argv[1])))
    print ("Video opened\nChoosing frames")
	
    #choosing the subset of frames from which video summary will be generateed
    frames = []
    i=0
    while(capture.isOpened()):
        if i%sampling_rate==0:
            capture.set(1,i)
            # print i
            ret, frame = capture.read()
            if frame is None :
                break
            #im = np.expand_dims(im, axis=0) #convert to (1, width, height, depth)
            # print frame.shape
            frames.append(np.asarray(frame))
        i+=1
    frames = np.array(frames)#convert to (num_frames, width, height, depth)

    print ("Frames chosen")
    print ("Length of video %d" % frames.shape[0])
    
    # REPLACE WITH APPROPRIATE FEATURES
    features = get_cnn_feat(frames)
    print ("Shape of features " + str(features.shape))
    
    # clustering: defaults to using the features
    print ("Clustering")

    # converting percentage to actual number
    num_centroids=int(percent*frames.shape[0]*sampling_rate/100)   
    
	# choose number of centroids for clustering from user required frames (specified in GT folder for each video)
    if percent==-1:
    	video_address=sys.argv[1].split('/')
    	gt_file=video_address[len(video_address)-1].split('.')[0]+'.mat'
    	video_address[len(video_address)-1]=gt_file
    	video_address[len(video_address)-2]='GT'
    	gt_file='/'.join(video_address)
    	num_frames=int(scipy.io.loadmat(gt_file).get('user_score').shape[0])
    	# automatic summary sizing: summary assumed to be 1/10 of original video
    	num_centroids=int(0.1*num_frames)

    if len(frames) < num_centroids:
        print ("Samples too less to generate such a large summary")
        print ("Changing to maximum possible centroids")
        num_centroids=frames.shape[0]

    #kmeans=KMeans(n_clusters=num_centroids).fit(features)
    kmeans=GaussianMixture(n_components=num_centroids).fit(features)
    print ("Done Clustering!")

    print ("Generating summary frames")
    summary_frames=[]

    # transforms into cluster-distance space (n_cluster dimensional)
    features_transform=kmeans.transform(features)
    frame_indices=[]
    for cluster in range(features_transform.shape[1]):
        print ("Frame number: %d" % (np.argmin(features_transform.T[cluster])*sampling_rate))
        frame_indices.append(np.argmin(features_transform.T[cluster]))
	
	# frames generated in sequence from original video
    frame_indices=sorted(frame_indices)
    summary_frames=[frames[i] for i in frame_indices]
    print ("Generated summary")
    
    if len(sys.argv)>5 and (int(sys.argv[5])==1 or int(sys.argv[6])==1):
        save_keyframes(frame_indices, summary_frames)

if __name__ == '__main__':
    main()