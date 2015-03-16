clear all
load('spam.mat');

% process1:

MeanM=mean(Xtrain(:,:),1);  % find mean along rows.
VarM=std(Xtrain(:,:),1);    % find stdvar along rows.

stdXtrain=zeros(3450,57);

for i=1:57
    stdXtrain(:,i)=(Xtrain(:,i)-MeanM(i))./VarM(i);
end


% process2:

logXtrain=log(Xtrain+0.1);


% process3:
binaryXtrain=Xtrain>0;

binaryXtrain=binaryXtrain+0;   % making it double again.
