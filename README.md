# Video-Summarization
In this project we use both keyframe extraction and video skimming for video summarization. For static keyframe extraction, we extract low level features using uniform sampling, image histograms, SIFT and image features from Convolutional Neural Network (CNN) trained on ImageNet. We also use different clustering methods including K-means and Gaussian clustering. We use video skims around the selected keyframes to make the summary fore fluid and comprehensible for humans. We take inspiration from the VSUMM method which is a prominent method in video summarization.

## Citation
If you find our code useful, please consider citing our work using the bibtex:
```
@article{jadon2019video,
  title={Video summarization using keyframe extraction and video skimming},
  author={Jadon, Shruti and Jasim, Mahmood},
  journal={arXiv preprint arXiv:1910.04792},
  year={2019}
}
```

##Methods Used:
1. Uniform Sampling
2. Image histogram
3. Scale Invariant Feature Transform
4. VSUMM:
This technique has been one of the fundamental techniques in video summarization in the unsupervised setup. The algorithm uses the standard K-means algorithm to cluster features extracted from each frame. Color histograms are proposed to be used in \cite{deAvila2011}. Color histograms are 3-D tensors, where each pixel’s values in the RGB channels determines the bin it goes into. Since each channel value ranges in 0 − 255, usually, 16 bins are taken for each channel resulting in a 16X16X16 tensor. Due to computational reasons, a simplified version of this histogram was computed, where each channel was treated separately, resulting in feature vectors for each frame belonging to R 48 . The nest step suggested for clustering is slightly different. But, the simplified color histograms give comparable performance to the true color histograms. The features extracted from VGG16 at the 2nd fully connected layer were tried, and clustered using kmeans.

5. ResNet16 on ImageNet
## Sample Architecture:
![alt text](https://github.com/shruti-jadon/Video-Summarization/blob/master/sample_cnn.png)

## Results:
![alt text](https://github.com/shruti-jadon/Video-Summarization/blob/master/image.png)
![alt text](https://github.com/shruti-jadon/Video-Summarization/blob/master/af1.png)
'''
To Run This Project
Use the following lines of code to download the SumMe dataset into the data folder. Refer to Michael Gygli's [page](https://people.ee.ethz.ch/~gyglim/vsum/).

```
chmod +x ./run_this.sh
./run_this.sh
```

Following is the list of dependencies: [imageio](https://imageio.github.io/), numpy, matplotlib, opencv3, scikit-learn. 
```
sudo pip install imageio
```
The same goes for numpy, matplotlib, tensorflow, scikit-learn. For opencv on Mac OSX,
```
brew tap homebrew/science && brew install --HEAD opencv3 --with-contrib --with-ffmpeg
brew install webp
```
The second command fixes an issue with importing opencv on Mac OSX.
'''
