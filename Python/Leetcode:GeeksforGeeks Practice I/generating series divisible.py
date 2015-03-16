__author__ = 'bozeng'


# assume we generate a series of integers that are divisible by 3,5:

# please check geeksforgeeks. you have a problem with this implementation.


def generate(n):
    result=[]

    divisor1=[3]
    divisor2=[5]

    pos1=0
    pos2=0


    while True:

        if divisor1[pos1]<divisor2[pos2]:
            result.append(divisor1[pos1])
            temp1=[divisor1[pos1]*3,divisor1[pos1]*5]
            divisor1.extend(temp1)
            pos1+=1
        elif divisor1[pos1]>divisor2[pos2]:
            result.append(divisor2[pos2])
            temp2=[divisor2[pos2]*3,divisor2[pos2]*5]
            divisor2.extend(temp2)
            pos2+=1
        else:
            result.append(divisor1[pos1])
            temp1=[divisor1[pos1]*3,divisor1[pos1]*5]
            divisor1.extend(temp1)
            temp2=[divisor2[pos2]*3,divisor2[pos2]*5]
            divisor2.extend(temp2)
            pos2+=1
            pos1+=1
        if result[-1]>n:
            break

    return divisor2



print(generate(100))


