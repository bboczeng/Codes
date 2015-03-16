__author__ = 'bozeng'


def repeatedDNA(string):
    if not string:
        return []

    result=[]

    dictionary={}

    for i in range(len(string)-10):
        tocheck=string[i:i+10]
        if tocheck not in dictionary:
            dictionary[tocheck]=1
        else:
            dictionary[tocheck]+=1


    for each in dictionary:
        if dictionary[each]>=2:
            result.append(each)

    return result

print(repeatedDNA("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

# come up with a simple solution for approaching.
# then, think of possible improvement.



def repeatedDNArolling(string):
    if not string:
        return []

    result=[]

    hashT={}

    def tonum(a):
        if a=="A":
            return 0
        if a=="C":
            return 1
        if a=="G":
            return 2
        if a=="T":
            return 3
    hashValue=-1
    for i in range(len(string)-9):
        if hashValue==-1:
            hashValue=0
            for j in range(10):
                hashValue=(ord(string[i+j])-ord('A'))+(hashValue<<2)
                print(j,"{0:b}".format(hashValue))
            print("{0:b}".format(hashValue))
        else:
            hashValue=((hashValue<<2)+ord(string[i+9])-ord('A'))%(1<<(2*10))
            print("{0:b}".format(hashValue))
        if hashValue in hashT:
            hashT[hashValue]=(1+hashT[hashValue][0],string[i:i+10])
        else:
            hashT[hashValue]=(1,string[i:i+10])



    for each in hashT:
        if hashT[each][0]>=2:
            result.append(hashT[each][1])

    return result



print(repeatedDNArolling("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))