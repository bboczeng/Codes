%clear all
addpath('data');
load('data/digit-dataset/train.mat');
load('data/digit-dataset/test.mat');


train_images_reshaped=(reshape(train_images(:,:,:),[],60000))';
test_images_reshaped=(reshape(test_images(:,:,:),[],10000))';

train_images_reshaped_sparse=sparse(train_images_reshaped);
test_images_reshaped_sparse=sparse(test_images_reshaped);


%%%
null_labels=zeros(10000,1);
traningmodel=train(train_labels(:),train_images_reshaped_sparse(:,:),['-s 2 -c ',num2str(10^(-6.6)),' -q']);
test_labels=predict(null_labels(:),test_images_reshaped_sparse(:,:),traningmodel,'-q');


id=1:10000;
matrix=[id',test_labels];

file_write=fopen('digit_kaggle.txt','w');
fprintf(file_write,'Id,Category\n');
fprintf(file_write,'%d,%d\n',matrix');
fclose(file_write);