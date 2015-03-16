Y=[1;1;0;0];
X=[0 3 1;1 3 1;0 1 1;1 1 1];
beta0=[-2;1;0];

-X*beta0
mu0=1./(1.+exp(-X*beta0))
nu0=mu0.*(1-mu0);
diagV0=diag(nu0);
lambda=0.07;
A0=2*lambda*eye(3)+X'*diagV0*X;
B0=2*lambda*beta0-X'*(Y-mu0);
beta1=beta0-inv(A0)*B0
mu1=1./(1.+exp(-X*beta1))
nu1=mu1.*(1-mu1);
diagV1=diag(nu1);

A1=2*lambda*eye(3)+X'*diagV1*X;
B1=2*lambda*beta1-X'*(Y-mu1);
beta2=beta1-inv(A1)*B1
mu2=1./(1.+exp(-X*beta2))