__author__ = 'bozeng'
def isValidSudoku(board):
        dictrow={}
        dictcol={}
        dictbox={}
        for i in range(9):
            dictrow={}
            dictcol={}
            dicbox={}
            for j in range(9):
                if board[i][j] not in dictrow:
                    dictrow[board[i][j]]=1
                elif board[i][j]!='.' and board[i][j] in dictrow:
                    return False
                if board[j][i] not in dictcol:
                    dictcol[board[j][i]]=1
                elif board[j][i]!='.' and board[j][i] in dictcol:
                    return False
                if board[i//3*3+j//3][i%3*3+j%3] not in dictbox:
                    dictbox[board[i//3*3+j//3][i%3*3+j%3]]=1
                elif board[i//3*3+j//3][i%3*3+j%3]!='.' and board[i//3*3+j//3][i%3*3+j%3] in dictbox:
                    return False

        return True