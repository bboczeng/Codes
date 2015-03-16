clear all
addpath('data');
load('data/digit-dataset/train.mat');
load('data/digit-dataset/test.mat');



reshuffle=randperm(60000);
train_images=train_images(:,:,reshuffle);
train_labels=train_labels(reshuffle);
train_images_reshaped=(reshape(train_images(:,:,:),[],60000))';

train_images_reshaped_sparse=sparse(train_images_reshaped);

accuracy_result=zeros(7,1);

count=1;

for each=[100 200 500 1000 2000 5000 10000]
    
    selection=randsample(1:50000,each);
    
    traningmodel=train(train_labels(selection),train_images_reshaped_sparse(selection,1:784),'-s 2 -q');

    [predicted,accuracy,somethingelse]=predict(train_labels(50001:60000,1),train_images_reshaped_sparse(50001:60000,1:784),traningmodel,'-q');
    
    accuracy_result(count)=accuracy(1);
    
    count=count+1;

end

trainingsize=[100 200 500 1000 2000 5000 10000];

figure
plot(trainingsize,accuracy_result,'b--o','LineWidth',3)
set(gca,'FontSize',24)
title('Training Result')
xlabel('Training size')
ylabel('Accuracy')