__author__ = 'bozeng'

def subsetsWithDup(S):
        answer=[[]]
        if len(S)==0:
            return answer

        S.sort()
        memory=[[]]
        temp=answer
        for j in range(len(S)):
            if j>0 and S[j]==S[j-1]:
                temp=memory
                memory=[]
            else:
                temp=answer
                memory=[]
            length=len(temp)
            for i in range(length):
                ttemp=temp[i][:]
                ttemp.append(S[j])
                answer.append(ttemp)
                memory.append(ttemp)

        return answer

print(subsetsWithDup([1,2,3,3,3,3]))