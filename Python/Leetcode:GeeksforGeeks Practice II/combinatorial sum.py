__author__ = 'bozeng'

def combinationSum2(candidates, target):

        length=len(candidates)
        result=[]
        candidates.sort()

        dict={}

        if length==0:
            return []

        def recursivefind(candidate,targ,temp,result):
            leng=len(candidate)
            if leng==0:
                return
            for i in range(leng):
                if candidate[i]==targ:
                    ttemp=temp[:]
                    ttemp.append(candidate[i])
                    if str(ttemp) not in dict:
                        dict[str(ttemp)]=1
                        result.append(ttemp)

                elif candidate[i]<targ:
                    ttemp=temp[:]
                    ttemp.append(candidate[i])
                    recursivefind(candidate[i+1:],targ-candidate[i],ttemp,result)

        recursivefind(candidates,target,[],result)



        return result

print(combinationSum2([10,1,2,7,6,1,5], 8))