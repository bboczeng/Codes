__author__ = 'bozeng'


def exist(board, word):
        if not board:
            return False
        if not word:
            return False
        row=len(board)
        if row==1:
            board=[board]
        col=len(board[0])
        length=len(word)

        visited={}

        def backtracking(i,j,count,visited):
            if count==length:
                return True

            if i<0 or j<0 or i>=row or j>=col:
                return False

            if (i,j) in visited and visited[(i,j)]==True:
                return False

            if board[i][0][j]==word[count]:
                visited[(i,j)]=True
                if backtracking(i,j+1,count+1,visited):
                    return True
                elif backtracking(i,j-1,count+1,visited):
                    return True
                elif backtracking(i+1,j,count+1,visited):
                    return True
                elif backtracking(i-1,j,count+1,visited):
                    return True
            visited[(i,j)]=False
            return False

        for i in range(row):
            for j in range(col):
                if backtracking(i,j,0,visited):
                    return True

        return False

print(exist(["aa"],"aa"))