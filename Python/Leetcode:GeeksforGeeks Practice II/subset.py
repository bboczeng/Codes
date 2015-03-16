__author__ = 'bozeng'
from copy import deepcopy

def subsetsWithDup( S):
        if len(S)==0:
            return []
        S.sort()
        result=[[]]
        oldlist=[]

        for i in range(len(S)):
            if i>0 and S[i]==S[i-1]:
                temp=deepcopy(oldlist)
                oldlist=[]
            else:
                temp=deepcopy(result)
                oldlist=[]
            for j in temp:
                j.append(S[i])
                result.append(j)
                oldlist.append(j)

        return result

print(subsetsWithDup([1,2,2,2,2,3]))