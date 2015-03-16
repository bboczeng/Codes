__author__ = 'bozeng'

import time

def swap(list,i,j):
    temp=list[j]
    list[j]=list[i]
    list[i]=temp


def permutate(list,i,n):
    if i==n:
        """print(list)"""
        return
    for j in range(i,n):
        swap(list,j,i)
        permutate(list,i+1,n)
        swap(list,i,j)
        """restore to the last step"""

List=[1,2,3,4,5,6,7,8,9]
start=time.time()
permutate(List,0,len(List))
end=time.time()
print(end-start)