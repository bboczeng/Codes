__author__ = 'bozeng'


def fourSum( num, target):
        if not num:
            return []
        num.sort()
        twosumdict={}

        for i in range(len(num)):
            for j in range(i+1,len(num)):
                tsum=num[i]+num[j]
                if tsum in twosumdict:
                    twosumdict[tsum].append((i,j))   # i < j
                else:
                    twosumdict[tsum]=[(i,j)]

        solution={}
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                tsum=num[i]+num[j]
                if target-tsum in twosumdict:
                    pairs=twosumdict[target-tsum]
                    for each in pairs:
                        (k, l)=each
                        if k!=i and k!=j and l!=i and l!=j:
                            temp=[num[i],num[j],num[l],num[k]]
                            temp.sort()
                            temp=tuple(temp)
                            if temp not in solution:
                                solution[temp]=True
        result=[]
        for each in solution:
            result.append(list(each))

        result.sort()
        return result


print(fourSum([-3,-2,-1,0,0,1,2,3],0))