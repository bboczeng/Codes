
%clear all
addpath('data');
load('data/digit-dataset/train.mat');
load('data/digit-dataset/test.mat');

reshuffle=randperm(60000);
train_images=train_images(:,:,reshuffle);
train_labels=train_labels(reshuffle);
train_images_reshaped=(reshape(train_images(:,:,:),[],60000))';

train_images_reshaped_sparse=sparse(train_images_reshaped);


cross_validation_set=30001:40000;
cross_validation_set_reshape=reshape(cross_validation_set,[],10)';

task=2;  % 0: tuning of C using cross validation; 1: finer tuning of C for cross-validatin, 2: validation set

if task==0 || task==1 
    
    count=1;
    
    if task==1
        tuningrange=-8:0.2:-5;
        result=zeros(16,1);
    end
    
    if task==0
        tuningrange=-14:0.5:4;
        result=zeros(37,1);
    end

    for cost=tuningrange
    % do a cross-validation 
        avaraged_accuracy=0;
        validation_set=1:10;
    
        for choice=1:10
            traningmodel=train(train_labels(cross_validation_set_reshape(validation_set(validation_set~=choice),:),1),train_images_reshaped_sparse(cross_validation_set_reshape(validation_set(validation_set~=choice),:),:),['-s 2 -c ',num2str(10^(cost))]);
            [predicted_lable,accuracy,prob_estimates]=predict(train_labels(cross_validation_set_reshape(choice,:),1),train_images_reshaped_sparse(cross_validation_set_reshape(choice,:),:),traningmodel,'-q');
            avaraged_accuracy=avaraged_accuracy+accuracy;
        end 
    
        avaraged_accuracy=avaraged_accuracy/10;
        result(count)=avaraged_accuracy(1);
        count=count+1;
    
    end


    Cvalue=tuningrange;
    figure
    plot(Cvalue,(100-result)/100,'b--o','LineWidth',3)
    set(gca,'FontSize',24)
    title('C Tuning Result with Cross Validation')
    xlabel('C Value (log10)')
    ylabel('Error Rate')
    
end

if task==2

% do validation witht the optimal C:

    traningmodel=train(train_labels(1:50000),train_images_reshaped_sparse(1:50000,:),['-s 2 -c ',num2str(10^(-6.6)),' -q']);
    [predicted_lable,accuracy,prob_estimates]=predict(train_labels(50001:60000),train_images_reshaped_sparse(50001:60000,:),traningmodel,'-q');

    fprintf('Validation Error Rate with Optimally tuned C value:');
    disp((100-accuracy(1))/100);
    
end
