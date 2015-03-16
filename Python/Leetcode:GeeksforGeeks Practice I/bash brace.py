__author__ = 'bozeng'


def bashbrace(string):
    if not string:
        return [[]]

    # do it recursively:


    def recursiveSol(strA):
        if not strA:
            return [[]]
        elif len(strA)==1:
            return [[strA[0]]]

        else:
            temp=[[]]
            i=0
            while i<len(strA):
                if strA[i]=="(":
                    count=1
                    for j in range(i+1,len(strA)):
                        if strA[j]=="(":
                            count+=1
                        elif strA[j]==")":
                            count-=1
                        if count==0:
                            break
                    subresult=recursiveSol(strA[i+1:j])

                    thistime=[]
                    for each in subresult:
                        for toadd in temp:
                            tmp=toadd[:]
                            tmp.extend(each[:])
                            thistime.append(tmp)
                    temp=thistime[:]
                    i=j+1
                elif strA[i]==",":
                    j=i+1
                    while j<len(strA):
                        if strA[j]==",":
                            subresult=recursiveSol(strA[i+1:j])
                            temp.extend(subresult[:])
                            i=j

                        j=j+1

                    subresult=recursiveSol(strA[i+1:])

                    temp.extend(subresult[:])
                    i=len(strA)
                else:
                    for each in temp:
                        each.append(strA[i])
                    i=i+1

            return temp

    result=recursiveSol(string)
    strresult=[]
    for each in result:
        strresult.append("".join(each))

    return strresult


print(bashbrace("(a,b)o(m,n)p,b"))