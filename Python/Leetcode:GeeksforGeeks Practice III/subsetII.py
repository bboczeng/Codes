__author__ = 'bozeng'


def subsetsWithDup(S):
        if not S:
            return [[]]

        S.sort()
        result=[[]]

        for i in range(len(S)):
            addpart=[]
            if i>0 and S[i]==S[i-1]:
                for item in oldresult:
                    add=item[:]
                    add.append(S[i])
                    addpart.append(add)
            else:
                for item in result:
                    add=item[:]
                    add.append(S[i])
                    addpart.append(add)

            oldresult=addpart

            result.extend(addpart)


        return result


print(subsetsWithDup([1,1,1,1,1,1,1,1]))