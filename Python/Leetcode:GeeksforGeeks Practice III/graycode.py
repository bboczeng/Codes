__author__ = 'bozeng'


def grayCode(n):
        if n==0:
            return []
        elif n==1:
            return [0,1]

        # understand the mechanism for generating gray code

        result=[0]*(2**n)

        result[1]=1

        count=2
        pos=1
        index=2

        while index<2**n:

            while index<2*count:
                result[index]=(result[2*count-index-1]+(1<<pos))
                index+=1

            count*=2
            pos+=1


        return result

print(grayCode(6))