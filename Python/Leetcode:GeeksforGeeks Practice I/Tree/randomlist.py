__author__ = 'bozeng'

def copyRandomList(self, head):

    if not head:
        return head

    created={}
    def recursiveList(node,created):
        if not node:
            return None

        if node in created:
            return

        newnode=RandomListNode(node.val)
        created[node]=newnode
        if node.next and node.next in created:
            newnode.next=created[node.next]
        else:
            newnode.next= recursiveList(node.next, created)

        if node.random and node.random in created:
            newnode.random=created[node.random]
        else:
            newnode.random = recursiveList(node.random, created)
        return newnode

    newhead=recursiveList(head, created)
    return newhead