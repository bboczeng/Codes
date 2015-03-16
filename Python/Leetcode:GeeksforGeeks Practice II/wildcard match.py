__author__ = 'bozeng'

def isMatch(s, p):
        if len(p)==0 and len(s)!=0:
            return False
        if len(s)==0 and len(p)==0:
            return True
        if len(s)==0:
            for i in range(len(p)):
                if p[i]!='*':
                    return False
            return True

        stackP=-1
        stackS=-1

        i=0
        j=0

        while i<len(s) and j<len(p):
            if s[i]==p[j] or p[j]=='?':
                j+=1
                i+=1
            elif p[j]=="*":
                stackS=i
                stackP=j
                j=stackP+1
                i=stackS
            elif stackP!=-1:
                j=stackP+1
                stackS+=1
                i=stackS
            else:
                return False

        if i==len(s):
            if j==len(p):
                return True
            elif p[j]=="*":
                return True

        if j==len(p):
            if i==len(s):
                return True
            elif p[j-1]=="*":
                return True

        return False

print(isMatch("aab","c*a*b"))