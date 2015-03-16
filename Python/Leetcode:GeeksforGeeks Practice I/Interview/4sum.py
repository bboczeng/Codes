__author__ = 'bozeng'


""" finds distinct elements A,B,C,D in an array []
return the indices of them
"""

def findIndices(array):
    if len(array)<4:
        print ("length of array must be greater than 4")
        return []

    summap={}

    # invariance: i is always smaller than j

    for i in range(len(array)):
        for j in range(i+1,len(array)):
            tempsum=array[i]+array[j]
            if tempsum not in summap:
                summap[tempsum]=[(i,j)]
            else:
                summap[tempsum].append((i,j))


    for i in range(len(array)):
        for j in range(i+1,len(array)):
            thissum=array[i]+array[j]
            if thissum in summap:
                for each in summap[thissum]:
                    if each[0]!=i and each[1]!=j:
                        result=[]
                        result.append(i)
                        result.append(j)
                        result.append(each[0])
                        result.append(each[1])


                        return result

    return []


print(findIndices([3,1,2,9,8]))


# find sums in an array: idea: use hash table for quick information presence check.