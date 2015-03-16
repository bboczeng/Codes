__author__ = 'bozeng'



def numDecodings( s):
        if not s:
            return 0
        num=[0]*len(s)

        if int(s[0])>=1 and int(s[0])<=9:
            num[0]+=1

        if len(s)==1:
            return num[0]

        if int(s[0:2])<=26 and int(s[0:2])>=10:
            num[1]+=1

        if int(s[1])>=1 and int(s[1])<=9:
            num[1]+=num[0]*1

        for index in range(2,len(s)):
            one,two=0,0
            if int(s[index])>=1 and int(s[index])<=9:
                one=1
            if int(s[index-1:index+1])>=10 and int(s[index-1:index+1])<=26:
                two=1
            num[index]=num[index-1]*(one)+num[index-2]*(two)

        return num

print(numDecodings("1234562321766"))
