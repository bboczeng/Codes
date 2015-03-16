__author__ = 'bozeng'


def validNumber(string):
    if not string:
        return False

    # trim leading and trailing zeros

    start=0
    end=len(string)-1

    while string[start]==" ":
        start+=1

    while string[end]==" ":
        end-=1

    state=0

    while start<=end:
        if string[start].isnumeric():

            if state==0 or state==0.5:
                state=1
            elif state==3 or state==4.5:
                state=4
            elif state==1:
                state=1
            elif state==4:
                state=4
            elif state==2:
                state=3.5
            elif state==3.5:
                state=3.5
            else:
                return False
        elif string[start]==".":

            if state==1:
                state=2
            elif state==0:
                state=2
            else:
                return False
        elif string[start]=="e" or string[start]=="E":

            if state==1:
                state=3
            elif state==3.5:
                state=3
            else:
                return False

        elif string[start]=="-" or string[start]=="+":

            if state==0:
                state=0.5
            elif state==3:
                state=4.5
            else:
                return False
        else:
            return False
        start+=1

    if state==1 or state==2 or state==3.5 or state==4:
        return True
    else:
        return False




print(validNumber("  3."))