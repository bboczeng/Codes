__author__ = 'bozeng'


def distinct(S,T):
    if not S:
        return 0
    if not T:
        return 0

    if len(S)<len(T):
        return 0
    if len(S)==len(T):
        return 1 if S==T else 0

    DPMatrix=[[0 for _ in range(len(S)+1)] for __ in range(len(T)+1)]

    DPMatrix[0][0]=1

    for i in range(1,len(S)+1):
        DPMatrix[0][i]=1

    for i in range(1,len(T)+1):
        for j in range(i,len(S)+1):
            if T[i-1]==S[j-1]:
                DPMatrix[i][j]=DPMatrix[i-1][j-1]+DPMatrix[i][j-1]
            else:
                DPMatrix[i][j]=DPMatrix[i][j-1]

    return DPMatrix[len(T)][len(S)]

print(distinct("aabab","ab"))