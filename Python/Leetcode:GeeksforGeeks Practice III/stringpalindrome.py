__author__ = 'bozeng'

# find all palindromes of a string, using back-tracking

def palindrome(s):
    if not s:
        return [[]]

    record=[[False]*(len(s)-x) for x in range(len(s))]

    for i in range(len(s)):
        record[0][i]=True

    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            record[1][i]=True

    for l in range(2,len(s)):
        for i in range(len(record[l])):
            if s[i]==s[i+l]:
                record[l][i]=record[l-2][i+1]



    result=[]

    def backtracking(i,temp):
        nonlocal result

        if i>=len(s) and temp:

            result.append(temp[:])

            return

        for test in range(i,len(s)):  # i is the start of this candidate:
            if record[test-i][i]:

                temp.append(s[i:test+1])

                backtracking(test+1,temp)
                temp.pop()

    backtracking(0,[])

    return result







print(palindrome("aab"))