__author__ = 'bozeng'

def isPalindrome(x):
        if x<0:
            return False
        elif x<10:
            return True

        ndigits=0
        num=x
        while num>0:
            ndigits+=1
            num=num//10

        lcount=ndigits
        num=x
        while lcount>1:
            lmask=10**(lcount-1)
            rdigit=num%10
            ldigit=num//(lmask)
            if ldigit!=rdigit:
                return False
            num=(num-lmask*(ldigit))//10
            lcount-=2
        return True

print(isPalindrome(1121112111211))