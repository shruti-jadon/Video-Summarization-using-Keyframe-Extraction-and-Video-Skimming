
# coding: utf-8

# In[ ]:

from keras.models import Sequential, Graph
from keras.layers import LSTM
from keras.layers import Merge, Convolution1D
from keras.layers import Input, Dense
import numpy as np, h5py 


# In[ ]:

num_frames = 100
num_features = 500
num_videos = 40

graph = Graph()
graph.add_input(name='input1', input_shape=(None,num_features))

graph.add_node(LSTM(256, input_shape=(None, num_features), return_sequences=True), name='lstm1', input='input1')
graph.add_node(LSTM(256, input_shape=(None, num_features),go_backwards = True,return_sequences=True), name='lstm2', input='input1')
graph.add_node(Convolution1D(nb_filter=256, filter_length=1, border_mode='same', input_shape=(None, 256+256+num_features)),inputs=['lstm1','lstm2','input1'],merge_mode='concat',name='conv1')

graph.add_output(name='output', input='conv1')


# In[ ]:

import scipy.io as sio
#trainX = videos_features
mat_contents = sio.loadmat('Air_Force_One.mat')
trainY = mat_contents['gt_score'].T

print trainY.shape


# In[ ]:

#model.fit(trainX, trainY, nb_epoch=15, batch_size=1, verbose=2)


# In[ ]:



