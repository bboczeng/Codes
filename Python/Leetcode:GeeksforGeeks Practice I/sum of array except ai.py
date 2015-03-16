__author__ = 'bozeng'


# sum of array a except a[i], for each i. generate the result in a new array.

def sum_except(a):
    if not a:
        return []

    result=[0]*len(a)


    for i in range(1,len(a)):
        result[i]=a[i-1]+result[i-1]


    # do it the otherway round

    mem=a[-1]

    for i in range(len(a)-2,-1,-1):
        result[i]=mem+result[i]
        mem=mem+a[i]

    return result

print(sum_except([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))