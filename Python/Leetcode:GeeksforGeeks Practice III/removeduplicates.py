__author__ = 'bozeng'


def removeDuplicates(A):
        if len(A)<=1:
            return
        cur=0
        probe=0

        while True:
            while probe<len(A) and A[probe]==A[cur]:
                probe+=1

            if probe==len(A):
                break
            cur+=1
            A[cur]=A[probe]

        print(A)

        print(cur+1)


removeDuplicates([1,1,2,2,2,3,3,3,3,3,4,5,5,6,7,8,8,9,9,10])