__author__ = 'bozeng'


def longsestPalisubs(string):
    if not string:
        return 0
    length=len(string)

    matrix=[[0 for __ in range(length)] for _ in range(length)]

    for size in range(length):
        for start in range(length-size):
            i=start
            j=start+size
            if i==j:
                matrix[i][j]=1
            elif j==i+1:
                matrix[i][j]=2 if string[i]==string[j] else 0
            elif string[i]==string[j]:
                matrix[i][j]=2+matrix[i+1][j-1]
            else:
                matrix[i][j]=max(matrix[i][j-1],matrix[i+1][j])


    return matrix[0][length-1]


print(longsestPalisubs("BBABCBCAB"))