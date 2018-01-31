import numpy as np
import os 
import cv2
import random
''' PATHS ''' 
HOMEVIDEOS='videos/'
from vgg16 import VGG16
from keras.preprocessing import image
from imagenet_utils import preprocess_input
from keras.models import Model
from sklearn.decomposition import PCA

def get_cnn_feat(frames_raw):
    frames=[]
    pca=PCA(n_components=500)
    for im in frames_raw:
        #print im.shape
        im = cv2.resize(im, (224, 224)).astype(np.float32)
        im[:,:,0] -= 103.939
        im[:,:,1] -= 116.779
        im[:,:,2] -= 123.68
        # print im.shape
        im = np.expand_dims(im, axis=0)
        #print im.shape
        frames.append(np.asarray(im))
    frames = np.array(frames)
    #print frames.shape

    base_model = VGG16(weights='imagenet', include_top=True)
    model = Model(input=base_model.input, output=base_model.get_layer('fc2').output)

    i = 0
    features = np.ndarray((frames.shape[0],4096),dtype=np.float32)
    for x in frames:
        #print x.shape
        features[i,:] = model.predict(x)
        i+=1
    return pca.fit_transform(features)

def get_color_hist(frames_raw, num_bins):
    print ("Generating linear Histrograms using OpenCV")
    channels=['b','g','r']
    
    hist=[]
    for frame in frames_raw:
        feature_value=[cv2.calcHist([frame],[i],None,[int(num_bins)],[0,256]) for i,col in enumerate(channels)]
        hist.append(np.asarray(feature_value).flatten())
    
    hist=np.asarray(hist)
    #print "Done generating!"
    print ("Shape of histogram: " + str(hist.shape))
    
    return hist