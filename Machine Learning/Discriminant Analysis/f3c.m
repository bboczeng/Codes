function y= f3c( x1,x2 )
%F3C Summary of this function goes here
%   Detailed explanation goes here
Sigma=[1 1;1 2];
mu1=[0;2];
mu2=[2;0];
detM=det(Sigma);
InvSigma=inv(Sigma);
VariableM=[x1;x2];
y=1/((2*pi)*sqrt(detM))*exp(-0.5*((VariableM-mu1).')*InvSigma*(VariableM-mu1))-1/((2*pi)*sqrt(detM))*exp(-0.5*((VariableM-mu2).')*InvSigma*(VariableM-mu2));


end

