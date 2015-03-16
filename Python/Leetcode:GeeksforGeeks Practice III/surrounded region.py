__author__ = 'bozeng'


def solve(board):
        vlength=len(board)
        if vlength==0:
            return
        hlength=len(board[0])

        # seach among the boundaries

        stack=[]
        visited={}

        for i in range(vlength):
            if board[i][0]=='O':
                stack.append((i,0))
            if board[i][hlength-1]=='O':
                stack.append((i,hlength-1))


        for i in range(hlength):
            if board[0][i]=='O':
                stack.append((0,i))
            if board[vlength-1][i]=='O':
                stack.append((vlength-1,i))

        while len(stack)>0:
            point=stack.pop()
            if point[0]<0 or point[0]>vlength-1 or point[1]<0 or point[1]>hlength-1:
                continue
            elif point not in visited:
                visited[point]=1
                if board[point[0]][point[1]]=='O':
                    board[point[0]][point[1]]='B'
                    stack.append((point[0]+1,point[1]))
                    stack.append((point[0]-1,point[1]))
                    stack.append((point[0],point[1]+1))
                    stack.append((point[0],point[1]-1))

        for i in range(vlength):
            for j in range(hlength):
                if board[i][j]=='B':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'


board=[['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]

solve(board)

print(board)