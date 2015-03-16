__author__ = 'bozeng'

import math

# what you should do is actually doing it with 2 sum.

def findcubicsum(n):

    if n<=0:
        return []

    uplimit=math.pow(n,1/3)

    dictionary={}

    candidates={}

    for i in range(1,int(uplimit)+1):
        dictionary[i**3]=True

    for j in range(1,n):
        for i in range(1,int(uplimit)+1):
            if (i**3)>j/2:
                break
            if j-(i**3) in dictionary:
                if j in candidates:
                    candidates[j]=1+candidates[j]
                else:
                    candidates[j]=1

    print(dictionary)

    result=[]

    for each in candidates:
        if candidates[each]==2:
            result.append(each)

    return result

print(findcubicsum(20000))