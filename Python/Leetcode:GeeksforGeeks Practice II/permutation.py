__author__ = 'bozeng'
def nextPermutation(num):

        length=len(num)
        pos=length-1

        while pos>0:
            if num[pos]>=num[pos-1]:
                break
            pos=pos-1

        if pos==0:
            # reverse the entire list
            num.reverse()
            return num

        pos=pos-1
        print(pos)
        pos2=length-1
        while pos2>pos:
            if num[pos2]>num[pos]:
                break
            pos2=pos2-1
        temp=num[pos2]
        num[pos2]=num[pos]
        num[pos]=temp

        i=length-1
        j=pos+1

        while j<=i:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
            i-=1
            j+=1


        return num

print(nextPermutation([5,4,7,5,3,2]))