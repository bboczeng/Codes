__author__ = 'bozeng'


def addbybit(a,b):

    x=a^b
    carry=a&b

    y=carry<<1

    while y!=0:

        carry=x&y
        x=x^y

        y=carry<<1

    return x

print(addbybit(1988,-20000000000000))