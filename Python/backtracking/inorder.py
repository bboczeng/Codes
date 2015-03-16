__author__ = 'bozeng'


def inorder(node):

    if not node:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)


def nonrecursive(root):

    node=root

    stack=[]

    while node:
        stack.append(node)
        node=node.left


    while stack:
        visit=stack.pop()
        print(visit.val)
        node=visit.right
        while node:
            stack.append(node)
            node=node.left


