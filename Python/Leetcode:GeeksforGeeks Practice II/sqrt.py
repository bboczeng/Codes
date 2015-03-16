__author__ = 'bozeng'

def sqrt(x):
        def recursivesqrt(nleft,nright,target):
            test=(nleft+nright)//2
            print(nleft,nright)
            test2=test*test
            if nleft==nright:
                return nleft
            if test2==target:
                return test
            elif test2>target:
                return recursivesqrt(nleft,test,target)
            elif test2<target:
                return recursivesqrt(test+1,nright,target)

        result=recursivesqrt(1,x,x)
        if result*result>x:
            return result-1
        return result


print(sqrt(5))