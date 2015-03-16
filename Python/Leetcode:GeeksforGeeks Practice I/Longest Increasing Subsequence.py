__author__ = 'bozeng'


def LISubsequence(array):
    if not array:
        return []

    result=[]

    DPresult=[(0,-1)]*len(array)  ## store (length,last position)

    for i in range(len(array)):
        if i==0:
            DPresult[i]=(1,-1)

        else:
            temp=1
            lastpos=-1
            for j in range(i):
                if array[j]<array[i] and DPresult[j][0]+1>temp:
                    temp=DPresult[j][0]+1
                    lastpos=j
            DPresult[i]=(temp,lastpos)

    temp=0
    lastpos=-1
    for i in range(len(array)):
        if DPresult[i][0]>temp:
            temp=DPresult[i][0]
            lastpos=i


    while lastpos!=-1:
        result.append(array[lastpos])
        lastpos=DPresult[lastpos][1]

    result.reverse()

    return result




print(LISubsequence([-1,2,100,100,101,3,4,5,-7]))