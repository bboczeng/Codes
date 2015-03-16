__author__ = 'bozeng'


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

Node1=ListNode(1)
Node2=ListNode(4)
Node3=ListNode(3)
Node4=ListNode(2)
Node5=ListNode(5)
Node6=ListNode(2)

Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
Node4.next=Node5
Node5.next=Node6


def partition(head, x):
        if not head:
            return head


        last=ListNode(0)
        last.next=head
        vhead=last

        current=last.next

        marker=None

        while True:

            if current==None:
                break

            if current.val>=x:
                if not marker:
                    marker=last

            elif marker:
                tmp=marker.next
                marker.next=current
                last.next=current.next
                current.next=tmp
                marker=current
                current=last.next
                continue


            last=current
            current=current.next

        return vhead.next

def makeList(list):
    if not list:
        return None
    vhead=ListNode(0)
    last=vhead
    for each in list:
        node=ListNode(each)
        last.next=node
        last=node

    return vhead.next



def printList(node):
    while node:
        print(node.val)
        node=node.next

printList(partition(makeList([1,4,3,2,5,2,6,7,8,9,1,1,2,3,0,-1,2]), 3))
