s=[-4:0.1:6];
t=[-4:0.1:6];

z=zeros(length(s),length(t));

for i= 1:length(s)
    for j= 1:length(t)
        z(i,j)=f3e(s(i),t(j));
    end
end

conMat=contour(t,s,z);
clabel(conMat)
