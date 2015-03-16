__author__ = 'bozeng'


# give array A[i], now adjust to B[i] so that each adjacent element in B[i] differ at most k, |B[i]-B[i-1]|<=k. Compute
# the total adjust cost Sum(|A[i]-B[i]|) and find a B[i] so that total cost is minimized.
# numbers in A[i] are from 0 to 100

def MinimumCost(lstA,k):
    assert k>=0, "relative different must be non-negative"
    if not lstA:
        return

    costs=[-1 for x in range(101)]
    oldcosts=[-1 for x in range(101)]

    for i in range(len(lstA)):
        if i==0:
            for j in range(101):
                costs[j]=abs(j-lstA[i])
        else:
            for j in range(101):
                mincost=(1<<31)-1
                thiscost=abs(j-lstA[i])
                for m in range(max(0,j-k),min(j+k,100)+1):
                    mincost=min(oldcosts[m]+thiscost,oldcosts[m]+thiscost,mincost)

                costs[j]=mincost
        oldcosts=costs[:]

    mincost=(1<<31)-1
    for cost in costs:
        mincost=min(cost,mincost)

    return mincost

print(MinimumCost([1,4,2,3],1))


def MinimumCostwithAnswer(lstA,k):
    assert k>=0, "relative different must be non-negative"
    if not lstA:
        return

    costs=[-1 for x in range(101)]
    oldcosts=[-1 for x in range(101)]

    results=[[-1 for x in range(101)] for i in lstA]

    for i in range(len(lstA)):
        if i==0:
            for j in range(101):
                costs[j]=abs(j-lstA[i])
        else:
            for j in range(101):
                mincost=(1<<31)-1
                minm=-1
                thiscost=abs(j-lstA[i])
                for m in range(max(0,j-k),min(j+k,100)+1):
                    if mincost>oldcosts[m]+thiscost:
                        mincost=oldcosts[m]+thiscost
                        minm=m

                results[i][j]=minm
                costs[j]=mincost
        oldcosts=costs[:]

    mincost=(1<<31)-1
    j=-1
    for i in range(len(costs)):
        if mincost>costs[i]:
            mincost=costs[i]
            j=i

    optimal=[]
    i=len(lstA)-1
    while i>=0:
        optimal.append(j)
        m=results[i][j]
        j=m
        i=i-1

    optimal.reverse()




    return mincost,optimal


print(MinimumCostwithAnswer([99,99,90,95],1))