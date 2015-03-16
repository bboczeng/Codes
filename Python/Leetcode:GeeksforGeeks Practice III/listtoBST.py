__author__ = 'bozeng'

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        # Do it reciprocal in order stack method:

        if not head:
            return None

        def count(node):
            num=0
            while node:
                num+=1
                node=node.next

            return num


        listnode=[head]

        def toBST(size,listnode):

            if size==0:
                return None

            left=toBST(size//2,listnode)
            node=TreeNode(listnode[0].val)
            listnode[0]=listnode[0].next
            right=toBST(size-size//2-1,listnode)
            node.left=left
            node.right=right
            return node

        return toBST(count(head),listnode)
