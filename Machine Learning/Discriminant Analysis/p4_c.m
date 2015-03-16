indices=find(train_label==5);
% transform the training data set:
train_images_reshaped=(reshape(train_image(:,:,:),[],60000))';

selected_data=train_images_reshaped(indices,:);

cov_data=cov(selected_data);

figure
mesh(cov_data)
view(90,90)
colorbar