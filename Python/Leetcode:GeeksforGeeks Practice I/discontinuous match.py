__author__ = 'bozeng'

def DisconMatch(strA,strB):
    if not strA:
        return 0
    if not strB:
        return 0
    if len(strA)>len(strB):
        return 0

    m=len(strA)
    n=len(strB)

    DPmatrix=[[(0,-1) for x in range(n)] for y in range(m)]  # DP will remember (number, index) for matches found

    for i in range(m):
        for j in range(n):
            if strA[i]==strB[j]:
                if j==0 and i==0:
                    DPmatrix[i][j]=(1,j)
                elif i==0:
                    DPmatrix[i][j]=(DPmatrix[0][j-1][0]+1,j)
                elif j<i:
                    DPmatrix[i][j]=(0,-1)
                else:
                    DPmatrix[i][j]=(DPmatrix[i-1][j-1][0]+DPmatrix[i][j-1][0],j)

            else:
                if j==0:
                    DPmatrix[i][j]=(0,-1)
                else:
                    DPmatrix[i][j]=(DPmatrix[i][j-1][0],-1)

    print(DPmatrix)
    return DPmatrix[m-1][n-1]

print(DisconMatch("cat","c99a0dasdsadcacat"))



