__author__ = 'bozeng'

def singleNumber(A):
        if not A:
            return 0
        find=0

        for i in range(len(A)):
            find = find ^ A[i]

        return find


print(singleNumber([5,6,1,1,2,2,3,3,4,4,5]))