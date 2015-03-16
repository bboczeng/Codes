__author__ = 'bozeng'

from collections import deque

## this file contains graph represenation:

## adjacency list is the preferred

class adjList:
    def __init__(self,node):
        self.data=node
        self.next=None
        self.weight=1

    def addWeight(self,weights):
        self.weight=weights


class Graph:
    def __init__(self,order):
        self.order=order
        self.nodes=[None for x in range(order)]


    def addAdjNode(self,node,adjnode):
        assert node>=0 and adjnode>=0, "node index must be non-negative"
        if node>=self.order or adjnode>=self.order:
            print("node index out of bounds")
            return

        toadd=adjList(adjnode)
        toadd.next=self.nodes[node]

        self.nodes[node]=toadd

    def addAdjNodewithWeight(self,node,adjnode,weights):
        assert node>=0 and adjnode>=0, "node index must be non-negative"
        if node>=self.order or adjnode>=self.order:
            print("node index out of bounds")
            return

        toadd=adjList(adjnode)
        toadd.addWeight(weights)
        toadd.next=self.nodes[node]

        self.nodes[node]=toadd

    def adjNodes(self,node):
        # return all adjacent nodes to a given node
        assert node>=0, "node index must be non-negative"
        if node>=self.order:
            print("node index out of bounds")
            return
        if self.nodes[node]==None:
            return None
        else:
            probe=self.nodes[node]
            while probe!=None:
                yield probe.data
                probe=probe.next

# directed graph

def constructFullGraph(order):
    graph=Graph(order)
    for i in range(order):
        for j in range(i+1,order):
            graph.addAdjNode(i,j)

    return graph


def constructSpecialGraph():
    graph=Graph(10)
    graph.addAdjNode(0,1)
    graph.addAdjNode(0,2)
    graph.addAdjNode(0,3)
    graph.addAdjNode(1,6)
    graph.addAdjNode(2,4)
    graph.addAdjNode(2,5)
    graph.addAdjNode(4,8)
    graph.addAdjNode(5,8)
    graph.addAdjNode(3,7)


    return graph


# tree and graph traversals using stacks and queues.

def DFSTraversal(graph):

    if not graph:
        return

    visited=[-1]*graph.order

    stack=[0]

    while stack:
        current=stack.pop()
        if visited[current]==1:
            continue
        else:
            visited[current]=1

        print(current,"->",end="")

        for adj in graph.adjNodes(current):
            if visited[adj]!=1:
                stack.append(adj)


def BFSTraversal(graph):

    if not graph:
        return

    visited=[-1]*graph.order

    queue=deque()

    queue.append(0)

    while queue:
        current=queue.popleft()
        if visited[current]==1:
            continue

        else:
            visited[current]=1

        print(current,"->",end="")

        for adj in graph.adjNodes(current):
            if visited[adj]!=1:
                queue.append(adj)







newgraph=constructFullGraph(10)
newgraph2=constructSpecialGraph()
print("DFS")
DFSTraversal(newgraph)
print("")
DFSTraversal(newgraph2)
print("")
print("BFS")
BFSTraversal(newgraph)
print("")
BFSTraversal(newgraph2)
