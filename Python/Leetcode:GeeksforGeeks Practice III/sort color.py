__author__ = 'bozeng'

def sortColors(A):
        # inplace and not using extra dictionary
        if not A:
            return A
        head=0
        tail=len(A)-1
        probe=0

        while A[tail]==2 and tail>=probe:
                tail-=1

        while probe<=tail:
            print(head,probe,tail)
            if A[probe]==0:
                A[head]=0
                head+=1
                probe+=1
            elif A[probe]==2:
                A[probe]=A[tail]
                A[tail]=2
                while A[tail]==2:
                    tail-=1
            else:
                probe+=1

        for probe in range(head,tail+1):
            A[probe]=1

        return A

print(sortColors([0,0,2,2,1,1,1,0,0,0,2,2,0,0,1]))