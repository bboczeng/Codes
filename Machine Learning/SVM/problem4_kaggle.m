clear all
addpath('data');
load('data/spam-dataset/spam_data.mat');



% cross-validation here:



train_labels=double(training_labels(:))';

train_data_sparse=sparse(training_data);
test_data_sparse=sparse(test_data);

null_labels=zeros(5857,1);

traningmodel=train(train_labels(:),train_data_sparse(:,:),['-s 2 -c ',num2str(10^(-0.5)),' -q']);

test_labels=predict(null_labels(:),test_data_sparse(:,:),traningmodel,'-q');


id=1:5857;
matrix=[id',test_labels];

file_write=fopen('spam_kaggle.txt','w');
fprintf(file_write,'Id,Category\n');
fprintf(file_write,'%d,%d\n',matrix');
fclose(file_write);
