__author__ = 'bozeng'


def removeDuplicates(A):
        if len(A)<=1:
            return len(A)

        cur=0
        count=0
        old=A[0]

        for probe in range(len(A)):
            if A[probe]==old:
                count+=1
            elif A[probe]!=old:
                inc=0
                while inc<min(2,count):
                    A[cur]=old
                    cur+=1
                    inc+=1
                count=1
                old=A[probe]

        inc=0

        while inc<min(2,count):
            A[cur]=old
            cur+=1
            inc+=1

        return A, cur

print(removeDuplicates([1,2,3,3,3,3,3,3,3,3,4,4,5,6,7,8,8,8,8,8,9,10,11]))