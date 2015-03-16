__author__ = 'bozeng'


def singleNumber(A):
        # we need a state machine:
        # from 00->01->10->00
        bit1=0
        bit2=0
        for i in A:
            oldbit1=bit1
            bit1=bit1^(i&(~bit2))
            bit2=(oldbit1&i)|(bit2&(~i))

        return bit1

print(singleNumber([3,3,3,4,17,17,17,17,4,4,5,5,5,6,6,6]))