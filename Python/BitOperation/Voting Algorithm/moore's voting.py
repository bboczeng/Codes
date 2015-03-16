__author__ = 'bozeng'



def voting(num):
    if len(num)==1:
        return num[0]
    cand=num[0]
    count=1

    for i in range(1,len(num)):
        if num[i]==cand:
            count+=1

        else:
            count-=1
            if count==0:
                cand=num[i]
                count=1

    return cand

list=[1,5,5,5,2,3,4,5]

print(voting(list))