function y = f3a( x1,x2 )
%F3A Summary of this function goes here
%   Detailed explanation goes here
Sigma=[2 0;0 1];
mu=[1;1];
detM=det(Sigma);
InvSigma=inv(Sigma);
VariableM=[x1;x2];
y=1/((2*pi)*sqrt(detM))*exp(-0.5*((VariableM-mu).')*InvSigma*(VariableM-mu));

end

