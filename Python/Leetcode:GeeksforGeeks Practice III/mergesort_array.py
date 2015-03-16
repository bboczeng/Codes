__author__ = 'bozeng'



def mergesort_array(array):
    if not array or len(array)==1:
        return array

    length=len(array)

    def merge(start,mid,end): # to merge two segments [start,mid] and [mid+1,end]
        if mid>=end:
            return
        temp=[]
        i=start
        j=mid+1
        while i<=mid and j<=end:
            if array[i]<array[j]:
                temp.append(array[i])
                i+=1
            else:
                temp.append(array[j])
                j+=1
        while i<=mid:
            temp.append(array[i])
            i+=1
        while j<=end:
            temp.append(array[j])
            j+=1
        # copy from temp to array
        for i in range(start,end+1):
            array[i]=temp[i-start]



    def mergesort(start,end):
        # [start,end] segment for merge sort
        if start>=end:
            return

        mid=(start+end)//2

        mergesort(start,mid)
        mergesort(mid+1,end)

        merge(start,mid,end)

    mergesort(0,length-1)

    return array

print(mergesort_array([1,2,3,4,5,-1,-10,9,3,556,-34,5,0]))


