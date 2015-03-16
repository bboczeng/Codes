__author__ = 'bozeng'


# the OJ wants it to be faster.

def wordbreak(s,dict):

    if not s:
        return []

    if not dict:
        return []

    # do it using DFS backtracking

    def backtracking(index,temp,result):

        if index==len(s):
            result.append(temp[:])
            return

        for i in range(index+1,len(s)+1):
            if s[index:i] in dict:
                newtemp=temp[:]
                newtemp.append(s[index:i])
                backtracking(i,newtemp,result)


    result=[]
    backtracking(0,[],result)
    return result

print(wordbreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))


def wordbreakfaster(s,dict):

    if not s:
        return []

    if not dict:
        return []

    # do it using DFS backtracking
    # do an early truncate:

    history={}

    for each in dict:
        for char in each:
            if char not in history:
                history[char]=1

    for each in s:
        if each not in history:
            return []



    def backtracking(index,temp,result):

        if index==len(s):
            result.append(temp[:])
            return

        for each in dict:
            length=len(each)
            if index+length<=len(s) and s[index:index+length]==each:
                newtemp=temp[:]
                newtemp.append(each)
                backtracking(index+length,newtemp,result)


    result=[]
    backtracking(0,[],result)
    return result

print(wordbreakfaster("catsanddog",["cat", "cats", "and", "sand", "dog"]))


def wordbreakDP(s,dict):