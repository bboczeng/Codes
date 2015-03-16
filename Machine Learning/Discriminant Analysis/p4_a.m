clear all
addpath('data');
load('digit-dataset/train.mat');
train_images_reshaped=(reshape(train_image(:,:,:),[],60000))';

cov_data=zeros(10,784,784);
mean_data=zeros(10,1,784);

for class=0:9 
    indices=find(train_label==class);
    % transform the training data set:
    selected_data=train_images_reshaped(indices,:);
    cov_data(class+1,:,:)=cov(selected_data);
    mean_data(class+1,:,:)=mean(selected_data,1);
end
