__author__ = 'bozeng'

from collections import deque
# this implements the basic operation of an AVL balanced binary search tree
from random import sample


class treeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=0


class AVLTree:

    def __init__(self):
        self.root=None
        self.count=0


    def __height(self,node):
        if not node:
            return -1

        else:
            return node.height

    def __rotateRootLeft(self,root):
        # recalculate heights after rotation

        assert type(root) is treeNode, "can only rotate treeNode objects"

        if not root:
            return

        if not root.left:
            return

        newroot=root.left
        temp=newroot.right
        root.left=temp
        newroot.right=root

        root.height=1+max(self.__height(root.left),self.__height(root.right))
        newroot.height=1+max(self.__height(newroot.left),self.__height(newroot.right))

        return newroot


    def __rotateRootRight(self,root):
        # recalculate heights after rotation

        assert type(root) is treeNode, "can only rotate treeNode objects"
        if not root:
            return

        if not root.right:
            return

        newroot=root.right
        temp=newroot.left
        root.right=temp
        newroot.left=root

        root.height=1+max(self.__height(root.left),self.__height(root.right))
        newroot.height=1+max(self.__height(newroot.left),self.__height(newroot.right))

        return newroot


    def __rightmost(self,node):


        current=node

        if not current:
            return None

        while current.right:
            current=current.right

        return current


    def __voilate(self,node):
        if not node:
            return False
        else:
            return abs(self.__height(node.left)-self.__height(node.right))>1

    def __rotate(self,node):
        if self.__height(node.left)>self.__height(node.right):
            if node.left and self.__height(node.left.left)>=self.__height(node.left.right):
                        # left-left case, rotate left.

                newnode=self.__rotateRootLeft(node)
                return newnode

            elif node.left and self.__height(node.left.right)>self.__height(node.left.left):
                        # zag-zig

                newleft=self.__rotateRootRight(node.left)
                node.left=newleft
                newnode=self.__rotateRootLeft(node)

                return newnode


        else:
            if node.right and self.__height(node.right.right)>=self.__height(node.right.left):
                        # left-left case, rotate left.

                newnode=self.__rotateRootRight(node)
                return newnode

            elif node.right and self.__height(node.right.left)>self.__height(node.right.right):
                        # zig-zag

                newright=self.__rotateRootLeft(node.right)
                node.right=newright
                newnode=self.__rotateRootRight(node)

                return newnode



    def put(self,val):

        if not self.root:
            self.root=treeNode(val)
            return

        def recursivePut(node,val):
            if not node:
                return treeNode(val)
            if val>node.val:
                node.right=recursivePut(node.right,val)
            elif val==node.val:
                return node
            else:
                node.left=recursivePut(node.left,val)

            # update height:

            # check for height violation:

            if self.__voilate(node):
                return self.__rotate(node) # do rotations. 4 cases:


            node.height=1+max(self.__height(node.left),self.__height(node.right))

            return node

        self.root=recursivePut(self.root,val)




    def delete(self,val):

        if not self.root:
            self.root=treeNode(val)
            return

        def recursiveDelete(node,val):
            if not node:
                return None
            if val>node.val:
                node.right=recursiveDelete(node.right,val)
            elif val==node.val:
                # there is something recursive happening
                if not node.left:
                    return node.right
                else:
                    newval=(self.__rightmost(node.left)).val
                    node.val=newval
                    node.left=recursiveDelete(node.left,newval)

            else:
                node.left=recursiveDelete(node.left,val)

            # update height:

            # check for height violation:

            if self.__voilate(node):
                # do rotations. 4 cases:
                return self.__rotate(node) # do rotations. 4 cases:



            node.height=1+max(self.__height(node.left),self.__height(node.right))

            return node

        self.root=recursiveDelete(self.root,val)




    def find(self,val):
        if not self.root:
            return False

        current=self.root
        while current:
            if val==current.val:
                return True
            if val<current.val:
                current=current.left
            else:
                current=current.right

        return False


    def __inorder(self):
        lst=[]
        if not self.root:
            return

        def recursiveInOrder(node,lst):
            if not node:
                return
            recursiveInOrder(node.left,lst)
            lst.append(node.val)
            recursiveInOrder(node.right,lst)

        recursiveInOrder(self.root,lst)

        return lst


    def __BFS(self):
        if not self.root:
            return

        result=[]

        queue=deque()

        queue.append((self.root,0))

        while queue:
            node,level=queue.popleft()

            if not node:
                continue

            queue.append((node.left,level+1))
            queue.append((node.right,level+1))

            if level>=len(result):
                result.append([])

            result[level].append(str(node.val))

        return result

    def __iter__(self):
        lst=self.__inorder()
        return iter(lst)


    def sort(self):
        return self.__inorder()

    def __str__(self):

        result=self.__BFS()

        if not result:
            return "Empty"

        return "\n".join([",".join(each) for each in result])

    def __contains__(self,val):
        return self.find(val)



# finish others. including one iterator.


avl1=AVLTree()

print("adding 1 to 10 randomly")

k=int(input("number of element you want to test with AVL:"))

lst=sample([x for x in range(k)],k)

print("insersion order:",lst)

for x in lst:
    avl1.put(x)

print("iterating begins")

for x in avl1:
    print("iterating: ",x)

print("iterating ends")

print("sorting")
print(avl1.sort())
print("tree representation")
print(avl1)

lst=sample([x for x in range(k)],k)

print("deletion order:",lst)

for x in lst:
    print("===")
    print("current tree total height:",avl1.root.height if avl1.root else -1)
    print("deleting",x)
    avl1.delete(x)
    print("sorting")
    print(avl1.sort())
    print("tree representation")
    print(avl1)

