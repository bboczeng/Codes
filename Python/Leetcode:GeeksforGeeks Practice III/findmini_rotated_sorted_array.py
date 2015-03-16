__author__ = 'bozeng'

def minrotated(array):
    if not array:
        return None

    def findmin(i,j):
        if i==j:
            return (i,array[i])
        else:
            mid=(i+j)//2
            if array[mid]>array[j]:
                return findmin(mid+1,j)
            elif array[mid]<array[j]:
                return findmin(i,mid)

    return findmin(0,len(array)-1)

print(minrotated([6,7,1,2,3,4,5]))

