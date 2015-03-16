__author__ = 'bozeng'

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def preorderTraversal(root):
        if not root:
            return []

        result=[]

        # do it iteratively, using stack as thought before (this is simpler, althogh it uses space)

        stack=[]

        node=root

        while node:
            result.append(node.val)
            stack.append(node)
            node=node.left

        while stack:
            node=stack.pop()
            node=node.right
            while node:
                result.append(node.val)
                print(node.val)
                stack.append(node)
                node=node.left

        return result


node1=TreeNode(3)
node2=TreeNode(1)
node3=TreeNode(2)

node1.right=node2
node2.left=node3

print(preorderTraversal(node1))