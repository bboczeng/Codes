__author__ = 'bozeng'


def maxNonAdj(a):
    if not a:
        return 0

    include=a[0]
    exclude=0

    for i in range(1,len(a)):
        newinclude= a[i]+exclude

        newexclude= max(exclude,include)

        exclude,include=newexclude,newinclude


    return max(include,exclude)

print(maxNonAdj([3,2,5,10,7,12,3,4,33,44,55,]))


