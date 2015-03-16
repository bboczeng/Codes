__author__ = 'bozeng'

def findMin(num):
    if not num:
        return None
    start=0
    end=len(num)-1
    while start<=end:
        if end-start==2:
            return min(num[end],num[start])
        if end-start==1:
            return num[end]
        mid=(start+end)//2

        if num[end]>num[start]:
            return num[start]
        if num[start]==num[end]:
            if num[mid]==num[start]:
                end=end-1
                start=start+1
            elif num[mid]>num[start]:
                start=mid+1
            else:
                end=mid
        else:
            if num[mid]<=num[end]:
                end=mid
            elif num[mid]>=num[start]:
                start=mid+1
            else:
                break # not possible


print(findMin([2,2,3,3,4,4,4,4,4,4,5,6,7,8,1,1,1,1,1]))