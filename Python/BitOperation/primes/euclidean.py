__author__ = 'bozeng'


def gcd(a,b):
    if a>b:
        return gcd(b,a)
    elif a==b:
        return a

    if a==1:
        return 1
    if a==0:
        return b

    return gcd(b%a,a)


print(gcd(72,90))