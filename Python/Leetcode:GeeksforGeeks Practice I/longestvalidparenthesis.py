__author__ = 'bozeng'


# Difficult

def longestvalidparenthe(s):


    # DP is possible.... please consider more . more carefully. . this you can do end at this.. type of DP. it is subtring optimization problem.

    if not s:
        return 0

    longest=[0]*len(s) #

    for i in range(1,len(s)):
        if s[i]=="(":
            longest[i]=0
        else:
            if s[i-1]=="(":
                if i-2>=0:
                    longest[i]=2+longest[i-2]
                else:
                    longest[i]=2
            else:
                if i-longest[i-1]-1>=0 and s[i-longest[i-1]-1]=="(":
                    if i-2-longest[i-1]>=0:
                        longest[i]=2+longest[i-1]+longest[i-2-longest[i-1]]
                    else:
                        longest[i]=2+longest[i-1]
                else:
                    longest[i]=0

    maxlength=0
    for i in range(len(longest)):
        maxlength=max(maxlength,longest[i])

    return maxlength




print(longestvalidparenthe(")()())()()("))


