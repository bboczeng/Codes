__author__ = 'bozeng'

def exist(board, word):
        vlength=len(board)
        visited={}
        result=[0]
        if vlength==0:
            return False

        hlength=len(board[0][0])

        def recursivefind(vindex,hindex,visited,count,result):
            if result[0]==1:
                return
            if vindex<0 or hindex<0 or vindex>=vlength or hindex>=hlength:
                return
            if (vindex,hindex) in visited:
                return
            if board[vindex][0][hindex]==word[count]:
                visited[(vindex,hindex)]=1
                if count==len(word)-1:
                    result[0]=1
                recursivefind(vindex+1,hindex,visited,count+1,result)
                recursivefind(vindex-1,hindex,visited,count+1,result)
                recursivefind(vindex,hindex+1,visited,count+1,result)
                recursivefind(vindex,hindex-1,visited,count+1,result)


        for i in range(vlength):
            for j in range(hlength):
                if board[i][0][j]==word[0]: # means the starting point is a match
                    recursivefind(i,j,{},0,result)
                    if result[0]==1:
                        return True


        return False

print(exist([["aa"]], "aa"))