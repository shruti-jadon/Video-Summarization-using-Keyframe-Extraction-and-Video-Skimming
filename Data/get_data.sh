#!/bin/bash
wget https://data.vision.ee.ethz.ch/cvl/SumMe/SumMe.zip
unzip SumMe.zip
rm -rf SumMe.zip

# converts space separated file names to underscore separated names
cd SumMe/videos
for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done

cd ../GT
for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done