__author__ = 'bozeng'

def spiralOrder(matrix):
        n=len(matrix)
        if n==0:
            return []

        result=[]
        (i,j)=(0,0)

        (llimit,rlimit,ulimit,dlimit)=(0,n-1,1,n-1)

        direct="r"

        k=0

        while k<n**2:

            if direct=='r':
                if j<rlimit:
                    result.append(matrix[i][j])
                    j+=1
                else:
                    direct='d'
                    result.append(matrix[i][j])
                    i+=1
                    rlimit-=1
            elif direct=='d':
                if i<dlimit:
                    result.append(matrix[i][j])
                    i+=1
                else:
                    direct='l'
                    result.append(matrix[i][j])
                    j-=1
                    dlimit-=1
            elif direct=='l':
                if j>llimit:
                    result.append(matrix[i][j])
                    j-=1
                else:
                    direct='u'
                    result.append(matrix[i][j])
                    i-=1
                    llimit+=1
            elif direct=='u':
                if i>ulimit:
                    result.append(matrix[i][j])
                    i-=1
                else:
                    direct='r'
                    result.append(matrix[i][j])
                    j+=1
                    ulimit+=1
            k=k+1


        return result


print(spiralOrder([[1]]))