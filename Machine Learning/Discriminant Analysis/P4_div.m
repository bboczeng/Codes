clear all
addpath('data');
load('digit-dataset/train.mat');
load('digit-dataset/kaggle.mat');
train_images_reshaped=(reshape(train_image(:,:,:),[],60000))';
kaggle_images_reshaped=(reshape(kaggle_image(:,:,:),[],5000))';

% class prior:
counts_hist=hist(train_label);
prior=counts_hist./60000;


    
    
this_train_label=train_label(:);
this_train_images_reshaped=train_images_reshaped(:,:);
    
inv_sigma=zeros(10,784,784);
mean_data=zeros(10,1,784);

for class=0:9 
    indices=find(this_train_label==class);
    selected_data=this_train_images_reshaped(indices,:);
        
        % calculate covariance and mean
    inv_sigma(class+1,:,:)=inv(cov(selected_data)+eye(784)*10000);
    mean_data(class+1,:,:)=mean(selected_data,1);
end
    
    % get averaged sigma
    

    % doing inversion of the covariance matrix:
    

test_result=zeros(5000,1);

pk=zeros(10,5000);
    
for k=0:9
        
    meandata=mean_data(k+1,:);
    inverse=squeeze(inv_sigma(k+1,:,:));
    priop=log(prior(k+1));

    for i=1:5000
        data_test=kaggle_images_reshaped(i,:);
        variable=(data_test-meandata);
        pk(k+1,i)=priop-1/2*variable*(inverse)*(variable.');
    end
    
        
end
    % find the maximum
for i=1:5000
    pdata=pk(:,i);
    test_result(i)=find(pdata==max(pdata))-1;
end
    

id=1:5000;
matrix=[id',test_result];

file_write=fopen('digit_kaggle.txt','w');
fprintf(file_write,'Id,Category\n');
fprintf(file_write,'%d,%d\n',matrix');
fclose(file_write);




