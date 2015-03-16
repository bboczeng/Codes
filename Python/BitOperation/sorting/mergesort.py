__author__ = 'bozeng'

""" i can not do it in place, for a merge sort in array. Probably this is the advantage of quicksort? """

def merge(list,left1,right1,left2,right2):

    temp=[0]*(right2-left1+1)
    i=left1
    j=left2
    k=0
    while i<=right1 and j<=right2:
        if list[i]<=list[j]:
            temp[k]=list[i]
            i+=1
        else:
            temp[k]=list[j]
            j+=1
        k+=1
    if i!=(right1+1):
        while i<=right1:
            temp[k]=list[i]
            k+=1
            i+=1

    elif j!=(right2+1):
        while j<=right2:
            temp[k]=list[j]
            k+=1
            j+=1

    list[left1:right2+1]=temp



def mergesort(list,left,right):
    if left>=right:
        return

    middle=(left+right)//2
    mergesort(list,left,middle)
    mergesort(list,middle+1,right)
    merge(list,left,middle,middle+1,right)


list=[1,2,3,8,4,5,6,7,19,21,8,9,10,11,12,12]

mergesort(list,0,len(list)-1)

print(list)



