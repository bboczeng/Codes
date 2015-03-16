__author__ = 'bozeng'


def combinationSum(candidates, target):
        if not candidates:
            return []

        result=[]
        def backtracking(start,remaining,temp,result):

            if remaining<0:
                return
            if remaining==0:
                result.append(temp[:])
                return

            for i in range(start,len(candidates)):
                temp.append(candidates[i])
                backtracking(i,remaining-candidates[i],temp,result)
                temp.pop()

        backtracking(0,target,[],result)

        return result

print(combinationSum([2,3,6,7],19))