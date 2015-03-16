function y = f3e( x1,x2 )
%F3D Summary of this function goes here
%   Detailed explanation goes here
Sigma1=[1 0;0 2];
Sigma2=[2 1;1 2];
mu1=[1;1];
mu2=[-1;-1];
detM1=det(Sigma1);
detM2=det(Sigma2);
InvSigma1=inv(Sigma1);
InvSigma2=inv(Sigma2);
VariableM=[x1;x2];
y=1/((2*pi)*sqrt(detM1))*exp(-0.5*((VariableM-mu1).')*InvSigma1*(VariableM-mu1))-1/((2*pi)*sqrt(detM2))*exp(-0.5*((VariableM-mu2).')*InvSigma2*(VariableM-mu2));



end

