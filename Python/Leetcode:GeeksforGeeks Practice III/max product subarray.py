__author__ = 'bozeng'


def product(A):
    if not A:
        return 0
    elif len(A)==1:
        return A[0]

    # need max and min together
    maxnum=[0]*len(A)
    minnum=[0]*len(A)

    maxnum[0]=A[0]
    minnum[0]=A[0]

    resultmax=maxnum[0]

    for i in range(1,len(A)):
        if A[i]>0:
            maxnum[i]=max(A[i],A[i]*maxnum[i-1])
            minnum[i]=min(A[i],A[i]*minnum[i-1])
        else:
            maxnum[i]=max(A[i],A[i]*minnum[i-1])
            minnum[i]=min(A[i],A[i]*maxnum[i-1])

        resultmax=max(resultmax,maxnum[i])

    return resultmax


print(product([100,-1,3]))