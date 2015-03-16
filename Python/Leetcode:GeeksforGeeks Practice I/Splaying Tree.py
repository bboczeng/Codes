__author__ = 'bozeng'


## the fundamental operations are rotateleft and rotateright.

# it is always true for maybe both splaying tree and AVL tree. understand the recursive logic chain behind those operations.

class TreeNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None


class SplayTree:
    def __init__(self):

        self.root=None

    def insert(self,key,value):

        if not self.root:
            self.root=TreeNode(key,value)
            return

        self.root=self.splaying(self.root,key)

        if key==self.root.key:
            self.root.value=value

        elif key<self.root.key:     ## so key's (supposed) parent was the current root. and it can very well have left and right subtrees.
            node=TreeNode(key,value)
            node.right=self.root    ## due to the properties of BST, those subtrees must be smaller than key (returned root must be the closest).
            node.left=self.root.left
            self.root.left=None
            self.root=node

        else:
            node=TreeNode(key,value)
            node.left=self.root
            node.right=self.root.right ## due to the properties of BST, those subtrees must be greater than key.
            self.root.right=None
            self.root=node


    def find(self,key):

        self.root=self.splaying(self.root,key)

        if self.root.key==key:
            return self.root.value

        return None


    def __contains__(self,key):

        return self.find(key)!=None



    def remove(self,key):

        if not self.root:
            print("empty tree")
            return

        self.root=self.splaying(self.root,key)

        if self.root.key!=key:
            return

        else:  # then we should delete the root

            # the traditional BST deletion is to swap with its inorder predecessor and delete recursively.

            if self.root.left==None:
                self.root=self.root.right

            else: # since now, every thing in the left subtree is smaller than key, everything right subtree larger.
                righttree=self.root.right
                # splaying up the largest element (closest to key) in the left subtree
                self.root=self.splaying(self.root.left,key)  # its right must be empty
                self.root.right=righttree

    # the purpose of splaying is to recursively:
    # move the node with key to root (of the subtree previously rooted at node). or, move the node before key
    # if key is not found to root of such.
    def splaying(self,node,key):

        if not node:
            return None

        if key==node.key:
            return node

        if key<node.key:
            if node.left==None:
                return node

            if key<node.left.key:
                node.left.left=self.splaying(node.left.left,key) # this is a grand parent situation now
                node=self.rotateRight(node)

            elif key>node.left.key:
                node.left.right=self.splaying(node.left.right,key)
                if node.left.right:
                    node.left=self.rotateLeft(node.left)

            if node.left:
                return self.rotateRight(node)

            return node


        elif key>node.key:
            if node.right==None:
                return node

            if key<node.right.key:
                node.right.left=self.splaying(node.right.left,key)
                if node.right.left:
                    node.right=self.rotateRight(node.right)

            elif key>node.right.key:
                node.right.right=self.splaying(node.right.right,key)
                node=self.rotateLeft(node)

            if node.right:
                return self.rotateLeft(node)

            return node


    def rotateLeft(self,node):  ## only deal with parent-child rotation
        if not node:
            return None

        child=node.right

        if not child:
            return node

        node.right=child.left
        child.left=node

        return child


    def rotateRight(self,node): ## only deal with parent-child rotation

        if not node:
            return None

        child=node.left

        if not child:
            return node

        node.left=child.right

        child.right=node

        return child

    def keys(self):

        def recursivePreorder(node):

            if not node:
                return

            yield node.key
            yield from recursivePreorder(node.left)
            yield from recursivePreorder(node.right)

        return recursivePreorder(self.root)


    def values(self):

        def recursivePreorder(node):
            if not node:
                return

            yield node.value

            yield from recursivePreorder(node.left)
            yield from recursivePreorder(node.right)

        return recursivePreorder(self.root)





splayTree=SplayTree()

splayTree.insert(12,'him')
splayTree.insert(10,'him2')
splayTree.insert(1,'him3')
splayTree.insert(3,'him4')
splayTree.insert(5,'him5')
splayTree.insert(100,'him6')

print(splayTree.find(3))

for x in splayTree.keys():
    print(x)
