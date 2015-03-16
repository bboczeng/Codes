__author__ = 'bozeng'


class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


def makeList(dlist):
    if not dlist:
        return None

    node=ListNode(dlist[0])
    pre=node
    head=node

    for i in range(1,len(dlist)):
        node=ListNode(dlist[i])
        pre.next=node
        pre=node

    return head

def printList(node):
    if not node:
        return "Empty"

    result=[]

    while node:
        result.append(str(node.val))
        node=node.next

    print("->".join(result))

def reverseBetween( head, m, n):
        if not head:
            return head
        assert n>=m, "argument error"

        count=1
        node=head
        vhead=ListNode(0)
        vhead.next=head
        prev=vhead

        while node and count<m:

            node=node.next
            prev=prev.next
            count+=1

        start=node
        second=start.next


        if not second:
            return vhead.next
        third=second.next


        while count<n and start:

            if not second:
                break
            second.next=start
            start=second
            second=third
            if not third:
                break
            third=third.next

            count+=1

        prev.next=start
        node.next=second

        return vhead.next

node1=makeList([4,5,7,8,9,10])

printList(node1)

node2=reverseBetween(node1,2,5)

printList(node2)