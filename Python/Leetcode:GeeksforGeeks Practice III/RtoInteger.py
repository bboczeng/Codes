__author__ = 'bozeng'

def romanToInt(s):
        if not s:
            return 0

        result=0

        map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        length=len(s)
        old=map[s[length-1]]

        for i in range(1,length):
            current=map[s[length-1-i]]
            if current>=old:
                result+=old
                old=current
            else:
                old-=current

        print(result+old)




romanToInt("XXIV")