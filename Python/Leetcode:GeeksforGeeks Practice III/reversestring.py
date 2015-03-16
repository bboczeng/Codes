__author__ = 'bozeng'

def reverseWords(s):
        if not s:
            return ""
        result=[]
        temp=[]
        for eachchar in s:
            if eachchar==" ":
                if temp:
                    result.append("".join(temp))
                    temp=[]
            else:
                temp.append(eachchar)
        if temp:
            result.append("".join(temp))
        if not result:
            return ""
        result.reverse()
        s=" ".join(result)

        return s


print(reverseWords("abs sda"))