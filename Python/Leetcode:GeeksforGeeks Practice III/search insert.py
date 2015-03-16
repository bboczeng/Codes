__author__ = 'bozeng'


def searchInsert(A, target):
        if not A:
            return 0

        start=0
        end=len(A)-1

        while True:
            if start>end:
                return
            if start==end:
                if A[start]>target:
                    return start
                elif A[start]==target:
                    return start
                else:
                    return start+1

            mid=(start+end)//2
            if A[mid]==target:
                return mid

            elif A[mid]>target:
                end=mid
            else:
                start=mid+1

print(searchInsert([1,3,5,6],2))