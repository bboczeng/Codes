__author__ = 'bozeng'
from collections import deque

def findSubstring( S, L):
        if not S:
            return []

        if not L:
            return []

        number=len(L)
        size=len(L[0])

        # first run

        if len(S)<size*number:
            return []
        record={}
        for each in L:
            if each not in record:
                record[each]=1
            else:
                record[each]+=1

        scanned={}

        result=[]

        # eliminate dictionary comparison.
        foundcount=0
        start=0
        end=0

        while end+size<=len(S):
            word=S[end:end+size]
            print("scanning",word)
            if word not in record:
                foundcount=0
                scanned={}
                start+=1
                end=start
                continue
            elif word not in scanned:
                scanned[word]=1
                foundcount+=1
                end+=size

            elif scanned[word]<record[word]:
                scanned[word]+=1
                foundcount+=1
                end+=size
            else: # over counting
                    # shrinking the left of window [
                    # instead of comparing the dictinary, you should keep a variable called count. and if count==len(record), you know you find everything.
                    # so count: does not count anything not in record, nor does it count anything excessive. and these are the two things you should know in the two problems and
                    # relevant problems.
                while True:
                    toremove=S[start:start+size]
                    if toremove==word:
                        start+=size
                        end+=size
                        break

                    if toremove in scanned:
                        scanned[toremove]-=1
                        foundcount-=1
                    start+=size

            print(start,end)
            if foundcount==number:
                print("get one!")
                result.append(start)
                scanned={}
                start=start+1
                end=start
                foundcount=0

        return result
print(findSubstring("abaababbaba",["ab","ba","ab","ba"]))