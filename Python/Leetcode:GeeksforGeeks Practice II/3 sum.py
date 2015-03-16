__author__ = 'bozeng'

def threeSum(num):
        if len(num)<3:
            return []
        num.sort()
        result=[]
        length=len(num)
        for i in range(length-2):
            if i>0 and num[i]==num[i-1]:
                continue
            j=i+1
            k=length-1
            while j<k:
                if num[j]+num[k]==-num[i]:
                    result.append([num[i],num[j],num[k]])
                    j=j+1
                    k=k-1
                    while num[j]==num[j-1] and j<k:
                        j=j+1
                    while num[k+1]==num[k] and j<k:
                        k=k-1

                elif num[j]+num[k]<-num[i]:
                    j=j+1
                else:
                    k=k-1
        return result

print(threeSum([-10,5,-11,-15,7,-7,-10,-8,-3,13,9,-14,4,3,5,-7,13,1,-4,-11,5,9,-11,-4,14,0,3,-10,-3,-7,10,-5,13,14,-5,6,14,0,5,-12,-10,-1,-11,9,9,1,-13,0,-13,-1,4,0,-7,8,3,14,-15,-9,-10,-3,0,-15,-1,-2,6,9,11,6,-14,1,1,-9,-14,6,7,10,14,2,-13,-13,8,6,-6,8,-9,12,7,-9,-11,4,-4,-4,4,10,1,-12,-3,-2,1,-10,6,-13,-3,-1,0,11,-5,0,-2,-11,-6,-9,11,3,14,-13,0,7,-14,-4,-4,-11,-1,8,6,8,3]))