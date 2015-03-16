__author__ = 'bozeng'


def getPermutation(n, k):
        if n==1:
            return 1
        factorial=[0]*(n+1)
        factorial[0]=1
        factorial[1]=1

        for i in range(2,n+1):
            factorial[i]=factorial[i-1]*i


        candidate=[str(x) for x in range(1,n+1)]
        result=[]

        position=n
        k=k-1
        while position>=1:
        # k is betwwen factorial[position] and factorial[position+1]
            multiple=k//factorial[position-1]
            remaining=k%factorial[position-1]



            result.append(candidate.pop(multiple))



            if remaining==0:
                result.extend(candidate)
                break
            k=remaining
            position-=1

        return "".join(result)



print(getPermutation(3,1))
print(getPermutation(3,2))
print(getPermutation(3,3))
print(getPermutation(3,4))
print(getPermutation(3,5))
print(getPermutation(3,6))