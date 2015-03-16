% Generating Random Variables %
clear all

R1data=normrnd(3,3,100,1);
R2data=0.5*normrnd(3,3,100,1)+normrnd(4,2,100,1);

meanR1=mean(R1data);
meanR2=mean(R2data);


covM=cov(R1data,R2data,1);


[V,D]=eig(covM);


combined=[R1data-meanR1, R2data-meanR2];

figure
scatter(R1data,R2data)
xlim([-15,15])
ylim([-15,15])


arrow([meanR1, meanR2],[meanR1+D(1,1)*V(1,1), meanR2+D(1,1)*V(2,1)])
arrow([meanR1, meanR2],[meanR1+D(2,2)*V(1,2), meanR2+D(2,2)*V(2,2)])

U=[V(:,2), V(:,1)];


newR1data=(U.')*(combined.');

figure
scatter(newR1data(1,:),newR1data(2,:))
xlim([-15,15])
ylim([-15,15])