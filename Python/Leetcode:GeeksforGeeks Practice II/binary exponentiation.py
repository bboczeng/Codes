__author__ = 'bozeng'


def exponen(base, exponent):
    if base==1:
        return 1
    if base==0:
        return 0

    result=1

    while exponent>0:
        if exponent&1:
            result=result*base
        exponent=exponent>>1
        base=base**2

    return result



print(exponen(3,3))