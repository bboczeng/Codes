__author__ = 'bozeng'


def generateParenthesis( n):
        if n==0:
            return []

        # do it using backtracking
        result=[]
        def backtracking(right_num,left_num,temp,result):

            if right_num>n or left_num>n:
                return

            if right_num==left_num and right_num==n:
                result.append("".join(temp))
                return

            if left_num>right_num:
                return

            temp.append('(')
            backtracking(right_num+1,left_num,temp,result)
            temp.pop()
            temp.append(')')
            backtracking(right_num,left_num+1,temp,result)
            temp.pop()

        backtracking(0,0,[],result)

        return result


print(generateParenthesis(3))
