Y=[1;1;0;0];
X=[0 3 1;1 3 1;0 1 1;1 1 1];
beta=[-2;1;0];
lambda=0.07;

count=1
result=zeros(20,1);
for steps=1:20
mu=1./(1.+exp(-X*beta));
nu=mu.*(1-mu);
diagV=diag(nu);

A=2*lambda*eye(3)+X'*diagV*X;
B=2*lambda*beta-X'*(Y-mu);
newbeta=beta-inv(A)*B;
beta=newbeta;

mu(mu==0) = 1e-9;
mu(mu==1) = 1-(1e-9);
    
result(count)=lambda*beta'*beta-(Y'*log(mu)+(1-Y')*log(1-mu));
count=count+1;
end

plot(result)
