__author__ = 'bozeng'


maze=[[1,0,1,1],[1,1,0,1],[0,1,0,0],[0,1,1,1]]


def findmaze(maze):
    if len(maze)==0:
        return

    def findpath(row,col):

        if row==len(maze)-1 and col==len(maze[0])-1 and maze[row][col]==1:
            maze[row][col]=2
            print(maze)
            return True
        elif row>=len(maze) or col>=len(maze[0]):
            return False
        elif maze[row][col]==0:
            return False
        else:
            maze[row][col]=2

            if findpath(row,col+1)==True:
                return True

            if findpath(row+1,col)==True:
                return True

            maze[row][col]=1

            return False


    if findpath(0,0)==False:
        print("no solution found")
        return


    # print maze with correct labeling
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==1:
                maze[i][j]=0
            elif maze[i][j]==2:
                maze[i][j]=1


findmaze(maze)

print(maze)
