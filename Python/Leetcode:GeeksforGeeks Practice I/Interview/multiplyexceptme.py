__author__ = 'bozeng'


""" multiply all elements except me
"""

def multiplyexceptme(array):
    if not array:
        return []

    if len(array)==1:
        return [0]

    leftmulti=[1]*len(array)
    rightmulti=[1]*len(array)

    for i in range(1,len(array)):
        leftmulti[i]=array[i-1]*leftmulti[i-1]


    for i in range(len(array)-2,-1,-1):
        rightmulti[i]=array[i+1]*rightmulti[i+1]


    result=[0]*len(array)

    for i in range(len(array)):
        result[i]=leftmulti[i]*rightmulti[i]

    return result

print(multiplyexceptme([2,3,1,4]))