clear all
load('YearPredictionMSD.txt');

trainingset=[YearPredictionMSD(1:463715,2:91),ones(463715,1)];
testset=[YearPredictionMSD(463716:515345,2:91),ones(51630,1)];
traininglabel=YearPredictionMSD(1:463715,1:1);
testlabel=YearPredictionMSD(463716:515345,1:1);

A=trainingset'*trainingset;
B=trainingset'*traininglabel;

beta=linsolve(A,B);


RSSterm=sum(testset*beta-testlabel);

RSS=sum(RSSterm.^2);


testy=testset*beta;
figure
stem(beta,'b--o','LineWidth',3)
set(gca,'FontSize',24)
title('beta')
xlabel('Feature')
ylabel('Value')

% zoomed in 
figure
stem(beta(1:90),'b--o','LineWidth',3)
set(gca,'FontSize',24)
title('beta')
xlabel('Feature')
ylabel('Value')