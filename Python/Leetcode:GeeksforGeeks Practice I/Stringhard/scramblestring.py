__author__ = 'bozeng'


def scramblestring(s1,s2):
    len1=len(s1)
    len2=len(s2)

    if len1!=len2:
        return False
    if len1==0:
        return True

    def recursiveFind(str1,str2):
        if len(str1)!=len(str2):
            return False

        if sorted(str1)!=sorted(str2):
            return False

        if str1==str2:
            return True

        if len(str1)<=3:
            return True

        for i in range(len(str1)-1):
            tmp1=str1[:i+1]
            tmp2=str1[i+1:]
            tmp3=str2[:i+1]
            tmp4=str2[i+1:]
            tmp5=str2[len(str1)-(i+1):]
            tmp6=str2[:len(str1)-(i+1)]

            if (recursiveFind(tmp1,tmp3) and recursiveFind(tmp2,tmp4)):
                return True
            if (recursiveFind(tmp1,tmp5) and recursiveFind(tmp2,tmp6)):
                return True


        return False

    return recursiveFind(s1,s2)



print(scramblestring("great","rgtae"))