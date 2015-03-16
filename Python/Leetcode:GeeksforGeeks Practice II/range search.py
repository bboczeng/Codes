__author__ = 'bozeng'

target=11

def findRangeRecursive(li,start,end):
            mid=(start+end)//2
            if start==end:
                if li[start]==target:
                    return [start,end]
                else:
                    return [-1,-1]

            rangeL=findRangeRecursive(li,start,mid)
            rangeR=findRangeRecursive(li,mid+1,end)

            if rangeL[0]==-1 and rangeR[0]==-1:
                return rangeL
            elif rangeL[1]==-1:
                return rangeR
            elif rangeR[0]==-1:
                return rangeL
            else:
                return [rangeL[0],rangeR[1]]

A=[1,2,3,4,4,4,4,4,6,7,8,8,9,9,9,9,10]
print(findRangeRecursive(A,0,len(A)-1))