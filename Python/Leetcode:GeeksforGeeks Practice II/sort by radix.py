__author__ = 'bozeng'


def sortradix(array,radix,level):

    if len(array)==1:
        return
    count=[0]*len(array)
    interim=[0]*len(array)
    denom=radix**level

    for i in range(len(array)):
        count[(array[i]//denom)%radix]+=1

    for i in range(1,len(array)):
        count[i]+=count[i-1]

    for i in range(len(array)-1,-1,-1):
        interim[count[(array[i]//denom)%radix]-1]=array[i]
        count[(array[i]//denom)%radix]-=1

    for i in range(len(array)):
        array[i]=interim[i]

    return


array=[12,18,9,24,10,3,2,1,0,23,24,22,19,16,15,14,14,15,15,17]

sortradix(array,5,0)
sortradix(array,5,1)

print(array)