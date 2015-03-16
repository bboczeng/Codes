__author__ = 'bozeng'


def combine( n, k):
        if n==0:
            return []

        assert k<=n, "k is larger than number of integers"

        result=[]
        choice=[x for x in range(1,n+1)]

        def backtracking(remaining,temp,index,result):
            if remaining==0:
                result.append(temp[:])
                return
            if n-index<remaining:
                return
            if not choice:
                return
            for i in range(index,n):
                temp.append(choice[i])
                backtracking(remaining-1,temp,i+1,result)
                temp.pop()

        backtracking(k,[],0,result)

        return result



print(combine(10,2))