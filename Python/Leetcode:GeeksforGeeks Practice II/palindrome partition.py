__author__ = 'bozeng'
def partition(s):
        def isPalindrome(string):
            length=len(string)
            if length==0:
                return False
            if length==1:
                return True
            i=0
            while i < length-1-i:
                if string[i]!=string[length-1-i]:
                    return False
                i=i+1
            return True

        answer=[]

        if len(s)==0:
            return []

        def partitionRecursive(answer,stri,temp):
            print(stri)
            if len(stri)==0:
                answer.append(temp)
                return
            for i in range(len(stri)+1):
                if isPalindrome(stri[:i]):
                    ttemp=temp[:]
                    ttemp.append(stri[:i])
                    partitionRecursive(answer,stri[i:],ttemp)


        partitionRecursive(answer,s,[])

        print(answer)

partition("aabsas")