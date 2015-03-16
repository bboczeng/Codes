__author__ = 'bozeng'


def isInterleave(s1, s2, s3):
        # using DP:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)

        if len3!=(len1+len2):
            return False

        if len3==0:
            return True

        DPmatrix=[[False for _ in range(len1+1)] for __ in range(len2+1) ]

        DPmatrix[0][0]=True

        for i in range(1,len1+1):
            DPmatrix[0][i]=DPmatrix[0][i-1] and s3[i-1]==s1[i-1]

        for i in range(1,len2+1):
            DPmatrix[i][0]=DPmatrix[i-1][0] and s3[i-1]==s2[i-1]

        for i in range(1,len2+1):
            for j in range(1,len1+1):
                lastword=s3[i+j-1]
                flag1=False
                flag2=False
                if s1[j-1]==lastword:
                    flag1=DPmatrix[i][j-1]
                if s2[i-1]==lastword:
                    flag2=DPmatrix[i-1][j]
                DPmatrix[i][j]=(flag1 or flag2)


        return DPmatrix[len2][len1]


##print(isInterleave("a","","a"))


def isInterleavebetterSP(s1, s2, s3):
        # using DP:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)

        if len3!=(len1+len2):
            return False

        if len3==0:
            return True

        DPmatrixold=[False for _ in range(len1+1)]

        DPmatrixold[0]=True

        for i in range(1,len1+1):
            DPmatrixold[i]=DPmatrixold[i-1] and s3[i-1]==s1[i-1]

        DPmatrix=DPmatrixold[:]

        for i in range(1,len2+1):
            DPmatrix[0]=(s3[i-1]==s2[i-1])
            for j in range(1,len1+1):
                lastword=s3[i+j-1]
                flag1=False
                flag2=False
                if s1[j-1]==lastword:
                    flag1=DPmatrix[j-1]
                if s2[i-1]==lastword:
                    flag2=DPmatrixold[j]
                DPmatrix[j]=(flag1 or flag2)
            DPmatrixold=DPmatrix[:]



        return DPmatrix[len1]


print(isInterleavebetterSP("a","","s"))