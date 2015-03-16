Y=double(ytrain(:));
X=[binaryXtrain(:,:),ones(3450,1)];
beta=ones(58,1)*0.05;

% padding offset 1 to it

lambda=1;
eta0=1e-3;

result=zeros(6000,1);
count=1;
i=1;
for steps=1:6000
    
    mu=1./(1.+exp(-X*beta));
    
    eta=eta0/count;

    A=eta*(X(i))'*(Y(i)-mu(i));
    B=-2*lambda*eta*beta;
    nextbeta=beta+A+B;
    
    beta=nextbeta;

    mu(mu==0) = 1e-9;
    mu(mu==1) = 1-(1e-9);
    
    result(count)=lambda*beta'*beta-(Y'*log(mu)+(1-Y)'*log(1-mu));
    count=count+1;

    i=i+1;
    if i>3450
        i=1
    end
    
end
steps=1:6000;
figure
plot(steps,result,'b--o','LineWidth',3)
set(gca,'FontSize',24)
title('Binary data, stochastic, eta~1/t')
xlabel('Steps')
ylabel('L2 Regularized Loss')