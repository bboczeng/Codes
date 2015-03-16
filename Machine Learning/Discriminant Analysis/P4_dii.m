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
            data_test=test_images_reshaped(i,:);
            variable=(data_test-meandata);
            pk(k+1,i)=priop-1/2*variable*(inverse)*(variable.');
        end
    
        
    end
    % find the maximum
    for i=1:5000
        pdata=pk(:,i);
        test_result(i)=find(pdata==max(pdata))-1;
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




