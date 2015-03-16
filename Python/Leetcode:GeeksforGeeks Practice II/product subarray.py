__author__ = 'bozeng'

def maxProduct( A):
        if len(A)==0:
            return 0
        tmax=A[0]
        tmin=A[0]
        finalmax=A[0]
        length=len(A)
        for i in range(1,length):
            print(tmax,tmin)
            if A[i]<0:

                (tmax,tmin)=(max(tmin*A[i],A[i]),min(tmax*A[i],A[i]))

            else:
                tmin=min(tmin*A[i],A[i])
                tmax=max(tmax*A[i],A[i])

            finalmax=max(finalmax,tmax)

        return finalmax

print(maxProduct([1,6,-10,-3,-4,5]))