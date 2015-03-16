__author__ = 'bozeng'

def minstation(graph):
    if len(graph)==0:
        return 0

    ncity=len(graph)

    global minStation
    minStation=ncity

    visited=[-1]*ncity

    def backtracking(city,numStation,numvisited):
        global minStation
        if numvisited==ncity:
            if(minStation>numStation):
                print(visited)
            minStation=min(minStation,numStation)
            return
        elif city==ncity:
            return
        else:
            # build a station here
            count=0
            memory=[]
            for i in range(ncity):
                if graph[city][i]==1 and visited[i]==-1: # connected and not serviced yet
                    count+=1
                    visited[i]=city
                    memory.append(i)
            backtracking(city+1,numStation+1,numvisited+count)

            # do not build one here

            for j in memory:
                visited[j]=-1

            backtracking(city+1,numStation,numvisited)

    backtracking(0,0,0)

    print(minStation)


example=[[1,1,0,0,0,1,0,1],
[1,1,1,0,0,1,0,0],
[0,1,1,1,1,0,0,0],
[0,0,1,1,1,0,1,0],
[0,0,1,1,1,1,0,0],
[1,1,0,0,1,1,1,1],
[0,0,0,1,0,1,1,0],
[1,0,0,0,0,1,0,1]]


minstation(example)