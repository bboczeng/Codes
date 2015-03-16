__author__ = 'bozeng'


def sqrt(x):

        if x==1 or x==0:
            return x

        guess=x
        oldguess=guess

        while True:
            guess=(oldguess+x/oldguess)//2
            if guess>=oldguess:
                break
            oldguess=guess
        if guess*guess<=x:
            return guess
        else:
            return guess-1


print(sqrt(99))