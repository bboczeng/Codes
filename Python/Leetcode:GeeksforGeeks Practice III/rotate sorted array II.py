__author__ = 'bozeng'


def search(A, target):
        if not A:
            return False

        def recursiveSearch(start,end):
            if start>end:
                return False
            if start==end:
                return A[start]==target

            mid=(start+end)//2
            if A[mid]==target:
                return True

            if A[mid]>A[start]:
                # case one:
                if target>=A[start] and target<A[mid]:
                    return recursiveSearch(start,mid-1)
                else:
                    return recursiveSearch(mid+1,end)

            if A[mid]<A[start]:
                if target>A[mid] and target<=A[end]:
                    return recursiveSearch(mid+1,end)
                else:
                    return recursiveSearch(start,mid-1)

            elif A[mid]==A[start]:
                if A[mid]!=A[end]:
                    return recursiveSearch(mid+1,end) # the break point must be on the second half
                else:
                    return recursiveSearch(start+1,end-1)  # not in the front nor end

        return recursiveSearch(0,len(A)-1)

print(search([3,1,1],2))