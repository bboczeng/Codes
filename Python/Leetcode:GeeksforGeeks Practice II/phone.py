__author__ = 'bozeng'

def letterCombinations(digits):
        result=[]
        digitlist=list(digits)

        mapping={'2':["a","b","c"],'3':["d","e","f"],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        def recursiveappend(remainingdigits,temp,result):

            if len(remainingdigits)==0:
                result.append("".join(temp))
                return
            digit=remainingdigits[0]
            print(digit)
            if digit not in mapping:
                return
            for char in mapping[digit]:
                tempt=temp[:]
                tempt.append(char)
                recursiveappend(remainingdigits[1:],tempt,result)

        recursiveappend(digitlist,[],result)
        return result


print(letterCombinations("23"))