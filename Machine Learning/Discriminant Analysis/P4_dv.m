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

% do a k=6 cross-validation. 

permuted_index_reshape=reshape(permuted_index,[],6)';

validation_set=1:6;

count=1;
error_rate=zeros(6,1);

average_error=zeros(21,1);

tuncount=1;

for tuning=-5:0.5:5

    for choice=1:6
        test_index=permuted_index_reshape(validation_set(choice),:);
        training_index=reshape(permuted_index_reshape(validation_set(validation_set~=choice),:),1,[]);
    
        this_train_label=training_labels(training_index);

        this_training_data=training_data(training_index,:);
    
        this_test_data=training_data(test_index,:);
    
        this_test_label=training_labels(test_index);
    
    
        for class=0:1 
            indices=find(this_train_label==class);
            selected_data=this_training_data(indices,:);
        
        % calculate covariance and mean
            inv_sigma(class+1,:,:)=inv(cov(selected_data)+eye(55)*(10^tuning));
            mean_data(class+1,:,:)=mean(selected_data,1);
        end
    
        test_result=zeros(862,1);
        pk=zeros(2,862);
    
    
        for k=0:1
        
            meandata=mean_data(k+1,:);
            inverse=squeeze(inv_sigma(k+1,:,:));
            priop=log(prior(k+1));

            for i=1:862
                data_test=this_test_data(i,:);
                variable=(data_test-meandata);
                pk(k+1,i)=priop-1/2*variable*(inverse)*(variable.');
            end
    
        
        end
    
        for i=1:862
            pdata=pk(:,i);
            test_result(i)=find(pdata==max(pdata))-1;
        end
    
    
        error_rate(count)=numel(find(test_result~=(this_test_label.')))/862;
    
        count=count+1;
    
    end
    
    average_error(tuncount)=mean(error_rate)
    
    tuncount=tuncount+1;
    

end

figure
semilogx(10.^[-5:0.5:5],average_error,'b--o','LineWidth',3)
set(gca,'FontSize',24)
title('Tuning Result')
xlabel('alpha')
ylabel('Cross Validation Error Rate')

   



