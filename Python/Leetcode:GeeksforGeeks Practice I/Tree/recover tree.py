__author__ = 'bozeng'

def recoverTree(root):

    if not root:
        return root
    # do in order traversal

    data=[None,None,None] # prev, swap1, swap2

    def inorder(node,data):
        if not node:
            return
        inorder(node.left,data)
        if not data[0]:
            data[0]=node
        else:
            if data[0].val>node.val:
                if not data[1]:
                    data[1]=data[0]
                    data[2]=node

                elif data[1]:
                    data[2]=node
                    return

            data[0]=node
        inorder(node.right,data)

    inorder(root,data)

    if not data[1] or not data[2]:
        print("no swap")
    else:
        temp=data[1].val
        data[1].val=data[2].val
        data[2].val=temp
    return root

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

root=TreeNode(1)
node1=TreeNode(0)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
root.left=node1
root.right=node3
node3.left=node2
node3.right=node4
node4.right=node5

node3.val=4
node4.val=3

recoverTree(root)

print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)
print(root.right.right.right.val)