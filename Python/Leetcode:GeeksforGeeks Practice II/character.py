__author__ = 'bozeng'

def lengthOfLastWord(s):
        if len(s)==0:
            return 0
        i,k,j=-1,-1,0
        while j<len(s):
            if s[j]!=' ' and i==-1:
                i=j
            if s[j]==' ' and j+1<len(s) and s[j+1]!=' ':
                i=j+1
            if s[j]!=' ' and j+1<len(s) and s[j+1]==' ':
                k=j
            j=j+1

        print (i,j,k)

        if i==-1:
            return 0
        if k<i:
            return len(s)-i
        elif k>=i:
            return k-i+1



res=lengthOfLastWord("a  ")
print (res)