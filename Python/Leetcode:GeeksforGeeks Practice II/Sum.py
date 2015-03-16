__author__ = 'bozeng'

def addBinary(a, b):
        lista=list(a)
        listb=list(b)

        lista.reverse()
        listb.reverse()


        length=max(len(lista),len(listb))

        listb.extend(['0']*(length-len(listb)))
        lista.extend(['0']*(length-len(lista)))


        i=0
        answer=[]
        carry=0
        while i<length:
            if lista[i]=='0' and listb[i]=='0':
                answer.append(str(0+carry))
                carry=0
            elif lista[i]=='1' and listb[i]=='1':
                answer.append(str(0+carry))
                carry=1
            else:
                if carry==1:
                    answer.append('0')
                else :
                    answer.append('1')
            i=i+1

        if carry==1:
            answer.append('1')
        answer.reverse()
        return "".join(answer)

print(addBinary("0","1"))