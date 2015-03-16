__author__ = 'bozeng'
def isPalindrome(x):
        if x==0:
            return True
        elif x<0:
            return False
        elif x<10:
            return True

        rank=0
        temp=x
        while True:
            rank=rank+1
            temp=temp//10
            if temp<1:
                break

        for i in range(rank):
            j=rank-i-1

            if j>i:

                if (x%10**(i+1))//10**i!=(x//10**j)%10:
                    return False

        return True

print(isPalindrome(1234567891))