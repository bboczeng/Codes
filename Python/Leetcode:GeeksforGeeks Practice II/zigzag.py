__author__ = 'bozeng'

def convert( s, nRows):
        if nRows==0:
            return ''
        elif nRows==1:
            return s
        result=[]
        for i in range(nRows):
            result.append([])

        length=len(s)
        i=0
        for j in range(length):
            result[i].append(s[j])
            if i==0:
                dire='d'
            elif i==nRows-1:
                dire='u'
            if dire=='d':
                i=i+1
            elif dire=='u':
                i=i-1
        temp=''
        for i in range(nRows):
            temp=temp+"".join(result[i])

        return temp
convert("PAYPALISHIRING", 3)