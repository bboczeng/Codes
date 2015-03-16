__author__ = 'bozeng'

def findMedianSortedArrays(A, B):
        m2=len(A)-1
        n2=len(B)-1
        m1=0
        n1=0
        m=m2-m1+1
        n=n2-n1+1
        k=(m+n)//2+1

        def findkelement(A,m1,m2,m,B,n1,n2,n,k):
            while True:

                if k>m+n:
                    return None
                if m==0:
                    return B[n1+k-1]
                if n==0:
                    return A[m1+k-1]
                if k==1:
                    return min(A[m1],B[n1])
                i=min(k-1,m)
                j=min(k-i,n)
                i+=(m1-1)
                j+=(n1-1)

                if A[i]<=B[j]:
                    k=k-(i+1-m1)
                    m1=i+1
                    n2=j
                else:
                    m2=i
                    k=k-(j+1-n1)
                    n1=j+1
                m=m2-m1+1
                n=n2-n1+1

        if (m+n)%2==0:
            return 1.0*(findkelement(A,m1,m2,m,B,n1,n2,n,k)+findkelement(A,m1,m2,m,B,n1,n2,n,k-1))/2

        return findkelement(A,m1,m2,m,B,n1,n2,n,k)

print(findMedianSortedArrays([1],[1,2,3]))