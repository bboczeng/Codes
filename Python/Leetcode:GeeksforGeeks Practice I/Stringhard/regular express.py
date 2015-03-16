__author__ = 'bozeng'


# check for DP solutions when you try to do backtracking

def regularmatch(s,p):
    if not s and not p:
        return True


    DPMatrix=[[False for _ in range(len(s)+1)] for __ in range(len(p)+1) ]

    DPMatrix[0][0]=True

    # initialize the 0 row:

    for i in range(1,len(p)+1):
        if p[i-1]=="*" and i>=2:
            DPMatrix[i][0]=DPMatrix[i-2][0]

    for i in range(1,len(p)+1):
        for j in range(1,len(s)+1):

            if p[i-1]==s[j-1] or p[i-1]==".":

                DPMatrix[i][j]=DPMatrix[i-1][j-1]

            elif p[i-1]=="*" and i>=2:
                prev=p[i-2]
                if prev==s[j-1] or prev==".":
                    DPMatrix[i][j] = DPMatrix[i-2][j-1] or DPMatrix[i][j-1] or DPMatrix[i-2][j]   ## even if you match, you can still skip it.
                else:
                    DPMatrix[i][j] = DPMatrix[i-2][j]

            else:
                DPMatrix[i][j]=False


    return DPMatrix[len(p)][len(s)]


print(regularmatch("aasdfasdfasdfasdfas","aasdf.*asdf.*asdf.*asdf.*s"))