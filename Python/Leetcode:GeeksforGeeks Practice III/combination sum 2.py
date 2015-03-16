__author__ = 'bozeng'

def combinationSum2(candidates, target):
        if not candidates:
            return []
        candidates.sort()
        result=[]
        def backtracking(start,remaining,temp,result):

            if remaining<0:
                return
            if remaining==0:
                result.append(temp[:])
                return

            i=start
            while i <len(candidates):
                temp.append(candidates[i])
                backtracking(i+1,remaining-candidates[i],temp,result)
                temp.pop()

                i+=1
                while i<len(candidates) and candidates[i]==candidates[i-1]:
                    i+=1


        backtracking(0,target,[],result)

        return result

print(combinationSum2([10,1,2,7,6,1,5],8))