__author__ = 'bozeng'

# find median of two sorted arrays.

# last method is by comparing medians.

# this method, we are using binary search for the median

# the problem is: it has to do with multiple number of arrays. (but two medians are doable. how about finding n array's medians?)...

def findMedian(a,b):

    # should implement it as find the kth

    int_min=-(1<<31)
    int_max=(1<<31)-1

    if not a and not b:
        return None

    def recursiveFind(start1,m,start2,n,k):
        i=((k-1)*(m))//(m+n)

        """ k has to be positive """

        j=k-i-1

        print(start1,m,start2,n,k,i,j)

        Ai_1=int_min if i==start1 else a[i-1]
        Ai=int_max if i==start1+m else a[i]
        Bj=int_max if j==start2+n else b[j]
        Bj_1=int_min if j==start2 else b[j-1]

        if Bj_1<=Ai and Ai<=Bj:
            return Ai
        elif Ai_1<=Bj and Bj<=Ai:
            return Bj

        if Ai<Bj:

            return recursiveFind(start1+i+1,m-i-1,start2,j,k-i-1)

        else:
            return recursiveFind(start1,i,start2+j+1,n-j-1,k-j-1)


    c=a+b

    return recursiveFind(0,len(a),0,len(b),5),sorted(c)


print(findMedian([1,2,3],[4,5,6,7]))







