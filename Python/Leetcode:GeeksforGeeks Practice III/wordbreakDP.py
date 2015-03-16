__author__ = 'bozeng'


def wordBreak(s, dict):
        if not dict:
            return False
        if not s:
            return False
        length=len(s)
        result=[False]*len(s)


        for i in range(length):
            for each in dict:
                leneach=len(each)
                if i-leneach>=0 and result[i-leneach] and s[i-leneach+1:i+1]==each:
                    result[i]=True
                if i==leneach-1 and s[0:i+1]==each:
                    result[i]=True
                if result[i]:
                    break
        return result[length-1]


print(wordBreak("leetcodecodeleet",["leet","code"]))