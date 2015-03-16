__author__ = 'bozeng'


def sortlist(headnode):
    if not headnode:
        return headnode

    length=0
    node=headnode
    while node:
        length+=1
        node=node.next




    def mergesort(headnode,length):

        size=2


        while size<length:
            node=headnode
            while node:
                merge(node,node.next)


            size=size*2



