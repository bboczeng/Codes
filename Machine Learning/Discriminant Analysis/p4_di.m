clear all
addpath('data');
load('digit-dataset/train.mat');
load('digit-dataset/test.mat');
train_images_reshaped=(reshape(train_image(:,:,:),[],60000))';
test_images_reshaped=(reshape(test_image(:,:,:),[],5000))';

% class prior:
counts_hist=hist(train_label);
prior=counts_hist./60000;

error_rate=zeros(9,1);

count=1;

for training_size=[100,200,500,1000,2000,5000,10000,30000,60000]
    sampling_indices= randsample(60000,training_size);
    
    this_train_label=train_label(sampling_indices);
    this_train_images_reshaped=train_images_reshaped(sampling_indices,:);
    
    cov_data=zeros(10,784,784);
    mean_data=zeros(10,1,784);

    for class=0:9 
        indices=find(this_train_label==class);
        selected_data=this_train_images_reshaped(indices,:);
        
        % calculate covariance and mean
        cov_data(class+1,:,:)=cov(selected_data);
        mean_data(class+1,:,:)=mean(selected_data,1);
    end
    
    % get averaged sigma
    average_sigma=zeros(784,784);
    average_sigma(:,:)=mean(cov_data,1)./10;

    % doing inversion of the covariance matrix:
    inv_signma=inv(average_sigma+eye(784)*100);

    test_result=zeros(5000,1);


    for i=1:5000
        data_test=test_images_reshaped(i,:);
        pk=zeros(10,1);

        for k=0:9
  
            pk(k+1)=log(prior(k+1))+data_test*(inv_signma)*(mean_data(k+1,:).')-1/2*mean_data(k+1,:)*(inv_signma)*(mean_data(k+1,:).');
    
        end
        
        % find the maximum 
        test_result(i)=(find(pk==max(pk))-1);
    end

    error_rate(count)=numel(find(test_result~=test_label))/5000
    
    count=count+1;
    
end

figure
semilogx([100,200,500,1000,2000,5000,10000,30000,60000],error_rate,'b--o','LineWidth',3)
set(gca,'FontSize',24)
title('Training Result')
xlabel('Training size')
ylabel('Error Rate')




