__author__ = 'bozeng'

class ListNode:
     def __init__(self, x):
            self.val = x
            self.next = None

def lprint(list):
    node=list
    string=""
    while node:
        print(node.val)
        string+=(str(node.val)+"->")
        node=node.next
    print(string)

def prepareList(array):
    if not array:
        return
    head=ListNode(array[0])
    oldx=head
    for i in range(1,len(array)):
        x=ListNode(array[i])
        oldx.next=x
        oldx=x
    oldx.next=None

    return head


def reorderList(head):
        if not head or not head.next:
            return head

        length=0
        node=head
        while node:
            node=node.next
            length+=1

        if length==2:
            return head


        pre=head
        count=1
        while count<(length-1)//2:
            pre=pre.next
            count+=1

        pre=pre.next
        cur=pre.next
        while cur:

            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt

        start=head
        last=pre
        count=length//2

        while count>0:
            temps=start.next
            templ=last.next
            start.next=last
            if count==1 and length%2==0:
                last.next=None
                break
            elif count==1 and length%2==1:
                print(last.val)
                print(temps.val)
                last.next=temps
                temps.next=None
                break
            else:
                last.next=temps

            start=temps
            last=templ
            count-=1

        return head


list1=prepareList([1,2,3])

lprint(list1)

list2=reorderList(list1)

lprint(list2)