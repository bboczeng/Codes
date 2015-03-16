__author__ = 'bozeng'
""" In an array where every element appears 3 times, find the element that appears only once """

def pickelement(array):
    if len(array)<=3:
        return None

    A=0
    B=0
    oldA=0
    oldB=0

    """ state transfer diagram: 00->01->10->00..."""

    for i in range(len(array)):

        B=oldB^(array[i]&(oldA|oldB))
        A=(oldA^(array[i]&(~oldB)))

        oldA=A
        oldB=B

    return A

array=[1,1,1,4,8,19,19,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
print(pickelement(array))