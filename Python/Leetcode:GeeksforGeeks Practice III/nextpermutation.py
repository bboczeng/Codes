__author__ = 'bozeng'


def nextPermutation(num):
        # one should be able to do it by keen observation .


        # find the start of a descending sequence from the tail

        if not num:
            return []

        def swap(i,j):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp

        def reverse(i,j):
            if i==j:
                return
            while i<j:
                swap(i,j)
                i+=1
                j-=1


        length=len(num)
        des_start=0
        for i in range(length-1,0,-1):
            if num[i-1]<num[i]:
                des_start=i
                break

        if des_start==0:
            reverse(0,length-1)
            return num

        place_to_change=des_start-1

        print(place_to_change,des_start)

        for i in range(length-1,place_to_change,-1):
            if num[i]>num[place_to_change]:
                swap(i,place_to_change)
                break


        reverse(des_start,length-1)

        return num


print(nextPermutation([1,2,3,4,6,5]))