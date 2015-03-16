__author__ = 'bozeng'


def findpeak(array):
    if not array:
        return

    length=len(array)

    if length==1:
        return (0,array[0])

    def find(i,j):
        if i==j:
            return (i,array[i])
        else:
            mid=(i+j)//2
            if mid==0:
                if array[1]<array[mid]:
                    return (mid,array[mid])
                else:
                    return find(mid+1,j)

            else:
                if array[mid]>array[mid+1] and array[mid]>array[mid-1]:

                    return (mid,array[mid])
                elif array[mid+1]>array[mid-1]:

                    return find(mid+1,j)
                else:

                    return find(i,mid)


    return find(0,length-1)


print(findpeak([1,2]))