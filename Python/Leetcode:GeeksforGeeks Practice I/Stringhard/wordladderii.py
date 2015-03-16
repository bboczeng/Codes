__author__ = 'bozeng'
from collections import deque
from collections import defaultdict
def findLadders(start,end,dict):
    if not start:
        return []


    worddict={}

    for each in dict:
        worddict[each]=1

    worddict[end]=1


    # you can do graph
    # or you can do backtracking

    # lets do graph


    # build links:


    letters="abcdefghijklmnopqrstuvwxyz"
    # the trick to word ladder

    def allneighbours(word):
        for i in range(len(word)):
            for x in letters:
                newword=word[:i]+x+word[i+1:]
                if newword in worddict:
                    yield newword


    queue=deque()

    queue.append((start,[start]))

    visited={}

    result=[]

    shortestlength=-1

    while queue:
        (node,chainlist)=queue.popleft()




        if node==end:
            if shortestlength==-1:
                shortestlength=len(chainlist)
            elif shortestlength<len(chainlist):
                continue
            result.append(chainlist)
            continue

        visited[node]=1

        if shortestlength!=-1 and shortestlength<=len(chainlist):
            continue


        for each in allneighbours(node):
            if each not in visited:
                temp=chainlist[:]
                temp.append(each)
                queue.append((each,temp))





    return result


def findLaddersANS( start, end, dic):
        dic=set(dic)
        dic.add(end)
        letters="abcdefghijklmnopqrstuvwxyz"
        level = {start}
        parents = defaultdict(set)
        while level and end not in parents:
            next_level = defaultdict(set)
            for node in level:
                for char in letters:
                    for i in range(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:   # avoid back edge...
                            next_level[n].add(node)
            level = next_level
            print(next_level)
            parents.update(next_level)
            print("parents",parents)
        res = [[end]]
        while res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res


print(findLaddersANS("hit","cog",["hot","dot","dog","lot","log"]))