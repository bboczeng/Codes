Y=double(ytrain(:));
X=[binaryXtrain(:,:),ones(3450,1)];
beta=ones(58,1)*0.05;

% padding offset 1 to it

lambda=1;
eta=1e-4;

result=zeros(600,1);
count=1
for steps=1:600
    
    mu=1./(1.+exp(-X*beta));

    A=eta*X'*(Y-mu);
    B=-2*lambda*eta*beta;
    nextbeta=beta+A+B;
    
    beta=nextbeta;

    mu(mu==0) = 1e-9;
    mu(mu==1) = 1-(1e-9);
    result(count)=lambda*beta'*beta-(Y'*log(mu)+(1-Y)'*log(1-mu));
    count=count+1;
    
end
steps=1:600;
figure
plot(steps,result,'b--o','LineWidth',3)
set(gca,'FontSize',24)
title('Binary data, batch')
xlabel('Steps')
ylabel('L2 Regularized Loss')