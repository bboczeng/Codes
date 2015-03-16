__author__ = 'bozeng'

# this is counterintuitive, but it works for this special case for paths bottom up in the triangle.

def minimumTotal(triangle):
        if not triangle:
            return 0
        result=triangle[-1][:]

        for bottom in range(len(triangle)-2,-1,-1):

            for i in range(bottom+1):

                result[i]=min(result[i],result[i+1])+triangle[bottom][i]


        return result[0]


print(minimumTotal([[-1],[2,3],[1,-1,-3]]))