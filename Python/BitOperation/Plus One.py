__author__ = 'bozeng'

def plusOne(digits):
        length=len(digits)
        if length==0:
            return [1]
        carry=1
        i=1
        while carry and length-i>=0:
            tmp=digits[length-i]+carry
            if tmp<10:
                digits[length-i]=tmp
                carry=0
            else:
                digits[length-i]=(tmp)%10
                carry=1
                i+=1
        if carry==1:
            new=[1]
            new.extend(digits)
            return new
        else :
            return digits

print(plusOne([9,9,9]))