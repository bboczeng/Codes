function y = f3b( x1,x2 )
%F3B Summary of this function goes here
%   Detailed explanation goes here
Sigma=[3 1;1 2];
mu=[-1;2];
detM=det(Sigma);
InvSigma=inv(Sigma);
VariableM=[x1;x2];
y=1/((2*pi)*sqrt(detM))*exp(-0.5*((VariableM-mu).')*InvSigma*(VariableM-mu));

end

