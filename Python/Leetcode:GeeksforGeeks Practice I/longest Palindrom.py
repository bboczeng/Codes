__author__ = 'bozeng'


#

def longestpalindrom(string):
    if not string:
        return 0

    # pre-process the string so that using expanding to check palindrome is easy

    newstring=['$']
    # "$" is used to mark the start and end of string.
    for i in range(len(string)):
        newstring.append(string[i])
        newstring.append('#')

    newstring.append('$')

    boundary=1
    center=1

    size=[0]*len(newstring)

    for i in range(1,len(newstring)-1): # because of padding of $
        mirror=2*center-i

        size[i]=min(size[mirror],boundary-i) if i<boundary else 1

        while newstring[i-size[i]]==newstring[i+size[i]]:
            size[i]+=1

        if i+size[i]-1>boundary:
            boundary=i+size[i]-1
            center=i

    max=0
    for i in range(len(size)):
        if max<size[i]:
            max=size[i]

    print(size)

    return max-1

print(longestpalindrom("BCBABCBABCAB"))