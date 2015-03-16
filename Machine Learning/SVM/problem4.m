clear all
addpath('data');
load('data/spam-dataset/spam_data.mat');


% cross-validation here:

reshuffle=randperm(5172);

training_data=training_data(reshuffle,:);
train_labels=double(training_labels(reshuffle))';

train_data_sparse=sparse(training_data);


cross_validation_set=1:5172;
% do a 6 fold validation
cross_validation_set_reshape=reshape(cross_validation_set,[],6)';

result=zeros(61,1);

count=1;

for cost=-15:0.5:15
    % do a cross-validation 
    avaraged_accuracy=0;
    validation_set=1:6;
    
    for choice=1:6
        sampling=reshape(cross_validation_set_reshape(validation_set(validation_set~=choice),:),[],1);
        traningmodel=train(train_labels(sampling),train_data_sparse(sampling,:),['-s 2 -c ',num2str(10^(cost)),' -q']);
        [predicted_lable,accuracy,prob_estimates]=predict(train_labels(cross_validation_set_reshape(choice,:)),train_data_sparse(cross_validation_set_reshape(choice,:),:),traningmodel,'-q');
        avaraged_accuracy=avaraged_accuracy+accuracy;
    end 
    
    avaraged_accuracy=avaraged_accuracy/6;
    result(count)=avaraged_accuracy(1);
    count=count+1;
    
end


Cvalue=-15:0.5:15;
figure
plot(Cvalue,(100-result)/100,'b--o')
set(gca,'FontSize',24)
title('C Tuning Result with Cross Validation')
xlabel('C Value (log10)')
ylabel('Error Rate')