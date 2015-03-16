__author__ = 'bozeng'


# Using Morris Traversal

class Solution:
# @param root, a tree node
# @return nothing, do it in place
def flatten(self, root):
    if not root:
        return

    # using Morris Traversal of BT
    node=root

    while node:
        if node.left:
            pre=node.left
            while pre.right:
                pre=pre.right
            pre.right=node.right
            node.right=node.left
            node.left=None
        node=node.right