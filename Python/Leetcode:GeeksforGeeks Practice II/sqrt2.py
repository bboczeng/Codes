__author__ = 'bozeng'

def sqrt2(n):
    if n==1:
        return n
    x=n
    y=1.0
    e=0.00000001
    while abs(x-y)>e:
        x=1.0*(x+y)/2
        y=1.0*n/x
        print(x,y)

    return (x+y)/2

print(sqrt2(2))