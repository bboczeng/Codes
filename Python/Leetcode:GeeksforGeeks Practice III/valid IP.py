__author__ = 'bozeng'


def restoreIpAddresses(s):
        if not s:
            return []

        BFSstack=[]
        BFSstack.append((0,0,[]))

        result=[]

        end=len(s)

        while BFSstack:
            start,count,temp=BFSstack.pop(0)
            if start==end:
                if count==4:
                    result.append(temp[:])
                    continue
                else:
                    continue

            if count>4:
                continue


            for i in range(start+1,end+1):
                if i-start>3:
                    break
                word=s[start:i]
                if int(word)>=0 and int(word)<=255:
                    if not (len(word)>1 and word[0]=='0'):
                        newtemp=temp[:]
                        newtemp.append(s[start:i])
                        BFSstack.append((i,count+1,newtemp))

        sresult=[]
        for each in result:
            sresult.append(".".join(each))

        return sresult


print(restoreIpAddresses("010010"))