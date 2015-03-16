__author__ = 'bozeng'

def countAndSay(n):
        res=[0]*n
        res[0]="1"
        i=1
        while i<n:
            s=res[i-1]
            count=0
            temp=[]
            for chr in s:
                if count==0:
                    count+=1
                elif chr==oldc:
                    count+=1
                else:
                    temp.append(str(count)+oldc)
                    count=1
                oldc=chr
            temp.append(str(count)+oldc)
            res[i]="".join(temp)
            i+=1

        return res


print(countAndSay(10))