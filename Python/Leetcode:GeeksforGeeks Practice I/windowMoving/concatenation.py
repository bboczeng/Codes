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

        queue=deque()

        def comparedict(dict1,dict2):
            if len(dict1)!=len(dict2):
                return False
            for each in dict1:
                if each not in dict2:
                    return False
                elif dict1[each]!=dict2[each]:
                    return False

            return True

        for start in range(0,len(S)-number*size+1,size):
            if start!=0:
                startword=queue.popleft()
                scanned[startword]-=1
                if scanned[startword]==0:
                    scanned.pop(startword)
            if start==0:
                for i in range(number):
                    word=S[start+i*size:start+i*size+size]
                    queue.append(word)
                    if word not in scanned:
                        scanned[word]=1
                    else:
                        scanned[word]+=1

            else:
                word=S[start+(number-1)*size:start+number*size]
                queue.append(word)
                if word not in scanned:
                    scanned[word]=1
                else:
                    scanned[word]+=1

            print(scanned,record)

            if comparedict(scanned, record):
                result.append(start)

        return result


# remember the window counting method ! (how does it work!) this is very similar to the window counting method. there can be many improvements.


print(findSubstring("abaababbaba",["ab","ba","ab","ba"]))


# do it better by skipping apparently not useful solutions. i am now checking all, but some solutions can be truncated earlier.

# this is a common idea that you should know. search for stringmatch but you should truncate early.