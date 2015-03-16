__author__ = 'bozeng'

def overlapfunction(pattern):
    if not pattern:
        return []

    overlap=[0]*len(pattern)

    length=0

    overlap[0]=0 # this is important because, the improper suffix has been discarded.

    i=1

    while i<len(pattern):
        if pattern[i]==pattern[length]:

            length+=1
            overlap[i]=length
            i+=1

        elif length>0:
            length=overlap[length-1]   # overlap for pattern[0:length] at pattern[length-1], 0 based index

        else:
            overlap[i]=0
            i+=1

    return overlap


def KMP_search(pattern,text):
    if not pattern or not text:
        return None

    overlap=overlapfunction(pattern)

    i=0
    j=0

    while i<=len(text)-(len(pattern)):

        if text[i+j]==pattern[j]:

            j+=1
            if j==len(pattern):
                print("found one at",i)
                length=overlap[j-1]
                i+=j-length
                j=length
        elif j>0:
            length=overlap[j-1]
            i+=j-length
            j=length
        else:
            i+=1





KMP_search("aaa","akaakaaafaaa")
