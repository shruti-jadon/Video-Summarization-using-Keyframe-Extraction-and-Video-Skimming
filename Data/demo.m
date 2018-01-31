%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Demo for the evaluation of video summaries
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% This script takes a random video, selects a random summary
% Then, it evaluates it and plots the performance compared to the human summaries
%
%%%%%%%%
% publication: Gygli et al. - Creating Summaries from User Videos, ECCV 2014
% author:      Michael Gygli, PhD student, ETH Zurich,
% mail:        gygli@vision.ee.ethz.ch
%%%%%%%%


%% PATHS 
addpath('./matlab/')
HOMEDATA='./GT/';
HOMEVIDEOS='./videos/';

%% Take a random video
videoList=dir([HOMEVIDEOS '/*.webm']);
[~,videoName]=fileparts(videoList(round(rand()*24+1)).name)

% In this example we need to do this to now how long the summary selection needs to be
gt_data=load([HOMEDATA videoName '.mat']) 
nFrames=length(gt_data.gt_score);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Example summary vector 
%   selected frames set to n (where n is the rank of selection) and the rest to 0
%   Here, we select a random summary of 15% length of the input video
%%%%%%%%
summary_selection=rand(nFrames,1)*20;
summary_selection(summary_selection<quantile(summary_selection,0.85))=0;
summary_selection=round(summary_selection);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Evaluate
%   get f-measure at 15% summary length
%   This is the score reported in "Creating Summaries from User Videos"
%%%%%%%%
[f_measure,summary_length]=summe_evaluateSummary(summary_selection,videoName,HOMEDATA)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Plot results
%%%%%%%%
methodNames={'Random'};
[ res_handle ] = summe_plotAllResults({summary_selection},methodNames,videoName,HOMEDATA);
