clear all
addpath('data');
load('digit-dataset/train.mat');

counts_hist=hist(train_label);
probability=counts_hist./60000;
