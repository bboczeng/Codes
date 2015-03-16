clear all
addpath('data');
load('spam-dataset/spam_data.mat');
training_labels=double(training_labels);
% class prior: this is a binary classificatiob
counts_hist=hist(training_labels);
prior=zeros(2,1);
prior(1)=counts_hist(1)/5172;
prior(2)=counts_hist(10)/5172;

permuted_index=randperm(5172);
    
inv_sigma=zeros(2,55,55);
mean_data=zeros(2,1,55);

    
this_train_label=training_labels(:);

this_training_data=training_data(:,:);
    
    
    
for class=0:1 
    indices=find(this_train_label==class);
    selected_data=this_training_data(indices,:);
        
        % calculate covariance and mean
    inv_sigma(class+1,:,:)=inv(cov(selected_data)+eye(55)*(0.1));
    mean_data(class+1,:,:)=mean(selected_data,1);
end
    
test_result=zeros(5857,1);
pk=zeros(2,5857);
    
    
for k=0:1
        
    meandata=mean_data(k+1,:);
    inverse=squeeze(inv_sigma(k+1,:,:));
    priop=log(prior(k+1));

    for i=1:5857
        data_test=test_data(i,:);
        variable=(data_test-meandata);
        pk(k+1,i)=priop-1/2*variable*(inverse)*(variable.');
    end
    
        
end
    
for i=1:5857
    pdata=pk(:,i);
    test_result(i)=find(pdata==max(pdata))-1;
end
    

    
id=1:5857;
matrix=[id',test_result];

file_write=fopen('spam_kaggle.txt','w');
fprintf(file_write,'Id,Category\n');
fprintf(file_write,'%d,%d\n',matrix');
fclose(file_write);


    



