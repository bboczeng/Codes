__author__ = 'bozeng'

def getPermutation(n, k):
        branchcount=[0]*n
        if n==0:
            return None
        if n==1:
            if k==1:
                return "1"
            else:
                return None

        branchcount[n-1]=1
        index=n-2

        while index>=0:
            branchcount[index]=branchcount[index+1]*(n-index)
            index=index-1

        print(branchcount)

        if k<1 or k>branchcount[0]:
            return None

        target=k
        candidate=[str(i) for i in range(1,n+1)]
        result=[]

        for i in range(1,n):
            for j in range(1,n-i+2):
                if j*branchcount[i]>=target:
                    print(i,j,j*branchcount[i],target)
                    result.append(candidate[j-1])
                    candidate.pop(j-1)
                    target=target-(j-1)*branchcount[i]
                    break
        print(result)
        result.append(candidate[0])
        answer="".join(result)

        print(answer)

print(getPermutation(2, 1))