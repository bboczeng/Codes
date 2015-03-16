__author__ = 'bozeng'


import random

def votingrandom(num):
    length=len(num)

    while True:
        index=random.randint(0,length-1)
        element=num[index]
        count=0
        print(index)
        for i in range(length):
            if num[i]==element:
                count+=1
        if count>length//2:
            break
    return element

list=[1,5,5,5,5,3,4,5]

print(votingrandom(list))