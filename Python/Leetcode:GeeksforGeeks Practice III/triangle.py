__author__ = 'bozeng'


def minimumTotal(triangle):
        if not triangle:
            return 0
        result=[0]*len(triangle)
        result[0]=triangle[0][0]

        for colnum in range(1,len(triangle)):
            for i in range(colnum+1):
                if i==0:
                    oldresult=result[0]
                    result[i]=triangle[colnum][i]+oldresult
                elif i==colnum:
                    result[i]=triangle[colnum][i]+oldresult
                else:
                    oldresulttemp=result[i]
                    result[i]=triangle[colnum][i]+min(result[i],oldresult)
                    oldresult=oldresulttemp
            print(result)
        minimum=result[0]

        for num in result:
            minimum=min(minimum,num)

        return minimum


print(minimumTotal([[-1],[2,3],[1,-1,-3]]))