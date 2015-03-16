__author__ = 'bozeng'

import copy

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def generate(s,t):
        '''recursion with left and right branches'''
        if s>t:
            return [None]

        if s==t:
            return [TreeNode(s)]

        result=[]

        for i in range(s,t+1):
            left=generate(s,i-1)
            right=generate(i+1,t)
            for l in left:
                for r in right:
                    tmp=TreeNode(i)
                    tmp.left=l
                    tmp.right=r
                    result.append(tmp)

        return result


def build(nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return
        for i in range(n):
            root = nodes[i]
            for left in build(nodes[:i]):
                for right in build(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root

    # @return a list of tree node
def generateTrees2( n):
        nodes = list(map(TreeNode, range(1, n + 1)))
        return list(map(copy.deepcopy, build(nodes)))

def generateTrees(n):
        return generate(1,n)


def treeprint(node):
    if not node:
        return ""

    s=[]

    def recursive(node,s):
        if not node:
            s.append("#")
            return

        s.append(str(node.val))
        recursive(node.left,s)
        recursive(node.right,s)

    recursive(node,s)

    return "".join(s)

for each in generateTrees2(3):
        print(each)
        print(treeprint(each))





