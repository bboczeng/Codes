__author__ = 'bozeng'



def selectionsort(list):
    if len(list)<2:
        return list
    for i in range(len(list),1,-1):
        index=0
        temp=list[index]
        for j in range(0,i):
            if list[j]>temp:
                index=j
                temp=list[index]

        list[index]=list[i-1]
        list[i-1]=temp

    return list

print(selectionsort([1,10,22,2,3,4,5]))