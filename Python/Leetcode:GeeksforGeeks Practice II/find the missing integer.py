__author__ = 'bozeng'

def firstMissingPositive(A):
        for i in range(len(A)):
            target=A[i]
            while target>=1 and target<len(A)+1 and A[target-1]!=target:
                new_target=A[target-1]
                A[target-1]=target
                target=new_target

        for i in range(len(A)):
            target=A[i]
            if target!=i+1:
                return i+1

        return 1+len(A)

print(firstMissingPositive([2,1,3,5,6,7,9,9,9,-10]))