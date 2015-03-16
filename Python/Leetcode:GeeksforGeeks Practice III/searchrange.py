__author__ = 'bozeng'

def searchRange(A, target):
        if not A:
            return [-1,-1]

        left=0
        right=len(A)-1

        def findR(left,right):
            while True:

                if left>right:
                    return -1
                if left==right:
                    if A[left]==target:
                        return left
                    else:
                        return -1
                mid=(left+right)//2

                if A[mid]>target:
                    right=mid

                elif A[mid]<target:
                    left=mid+1

                else:
                    if mid+1<len(A) and A[mid+1]>target:
                        return mid
                    else:
                        left=mid+1

        def findL(left,right):
            while True:

                if left>right:
                    return -1
                if left==right:
                    if A[left]==target:
                        return left
                    else:
                        return -1
                mid=(left+right)//2

                if A[mid]>=target:
                    right=mid

                elif A[mid]<target:
                    left=mid+1




        while True:
            if left>right:
                return [-1,-1]
            if left==right:
                if A[left]==target:
                    return [left,right]
                else:
                    return [-1,-1]

            mid=(left+right)//2

            if A[mid]<target:
                left=mid+1
            elif A[mid]>target:
                right=mid
            else:
                if A[left]==target and A[right]==target:
                    return [left, right]
                elif A[left]==target:
                     right=findR(mid,right)

                elif A[right]==target:
                    left=findL(left,mid)

                else:
                    right=findR(mid,right)
                    left=findL(left,mid)

                return [left,right]







print(searchRange([5,5,5,5,5,5,6,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,10],8))