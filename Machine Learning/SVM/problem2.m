
% geneate confusion matrix for each training size:

clear all
addpath('data');
load('data/digit-dataset/train.mat');
load('data/digit-dataset/test.mat');

reshuffle=randperm(60000);
train_images=train_images(:,:,reshuffle);
train_labels=train_labels(reshuffle);
train_images_reshaped=(reshape(train_images(:,:,:),[],60000))';

train_images_reshaped_sparse=sparse(train_images_reshaped);



for each=[100 200 500 1000 2000 5000 10000]

    selection=randsample(1:50000,each);
    
    traningmodel=train(train_labels(selection,1),train_images_reshaped_sparse(selection,:),'-s 2 -q');

    predicted=predict(train_labels(50001:60000,1),train_images_reshaped_sparse(50001:60000,:),traningmodel,'-q');
    
    confusion_matrix=zeros(10,10);
    
    count_matrix=zeros(10,1);

    
    for i=1:10000
        confusion_matrix(train_labels(50000+i)+1,predicted(i)+1)=confusion_matrix(train_labels(50000+i)+1,predicted(i)+1)+1;
        count_matrix(train_labels(50000+i)+1)=count_matrix(train_labels(50000+i)+1)+1;
    end
    
    for digit=1:10
        confusion_matrix(digit,:)=confusion_matrix(digit,:)/count_matrix(digit);
    end
    
    figure
    
    imagesc(confusion_matrix);
    
    colormap(flipud(summer));
    
    % plot the checker box
    textStrings = num2str(confusion_matrix(:),'%0.2f');  %# Create strings from the matrix values
    textStrings = strtrim(cellstr(textStrings));  %# Remove any space padding
    [x,y] = meshgrid(1:10);   %# Create x and y coordinates for the strings
    hStrings = text(x(:),y(:),textStrings(:),...      %# Plot the strings
                'HorizontalAlignment','center');
    midValue = mean(get(gca,'CLim'));  %# Get the middle value of the color range
    textColors = repmat(confusion_matrix(:) > midValue,1,3);  %# Choose white or black for the
                                             %#   text color of the strings so
                                             %#   they can be easily seen over
                                             %#   the background color
    set(hStrings,{'Color'},num2cell(textColors,2));  %# Change the text colors
    set(gca,'LineWidth',3);
    set(gca,'FontSize',24)
    set(gca,'XTick',1:10,...                         %# Change the axes tick marks
        'XTickLabel',{'0','1','2','3','4','5','6','7','8','9'},...  %#   and tick labels
        'YTick',1:10,...
        'YTickLabel',{'0','1','2','3','4','5','6','7','8','9'},...
        'TickLength',[0 0]);
    title(strcat('Training Size: ',num2str(each)));
    xlabel('Predicted Label');
    ylabel('True Label');
    
end