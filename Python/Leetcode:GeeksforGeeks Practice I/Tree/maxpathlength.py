__author__ = 'bozeng'

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if not root:
            return 0

        result=[0]

        def recursiveMax(node,result)
            if not node:
                return 0

            leftlongest=recursiveMax(node.left, result)
            rightlongest=recursiveMax(node.right, result)
            thismax=max(leftlongest+node.val,rightlongest+node.val,rightlongest+node.val+leftlongest,node.val)
            result[0]=max(thismax,result[0])
            return max(node.val,leftlongest+node.val,rightlongest+node.val)

        recursiveMax(root,result)

        return result[0]
