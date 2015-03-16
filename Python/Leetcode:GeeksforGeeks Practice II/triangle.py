__author__ = 'bozeng'

def minimumTotal(triangle):
        if len(triangle)==0:
            return 0
        result=[0]*len(triangle)
        result[0]=triangle[0][0]
        for i in range(1,len(triangle)):
            oldresult=result[:]
            for j in range(i+1):
                if j==0:
                    result[j]=oldresult[0]+triangle[i][j]
                elif j==i:
                    result[j]=oldresult[j-1]+triangle[i][j]
                else :
                    result[j]=min(oldresult[j-1]+triangle[i][j],oldresult[j]+triangle[i][j])


        return result


print(minimumTotal([[-10]]))