__author__ = 'bozeng'

def pow(x, n):


    def recursivepow(x,m):
        if m==0:
            return 1
        if m==1:
            return x
        if m==2:
            return x*x

        left=recursivepow(x,m//2)
        if m%2==0:
            right=left
        else:
            right=left*x
        return left*right

    if n>=0:
        return recursivepow(x,n)
    else:
        return 1/recursivepow(x,-n)

print(pow(3, 99))