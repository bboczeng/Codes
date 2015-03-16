__author__ = 'bozeng'

class ListNode:
     def __init__(self, x):
            self.val = x
            self.next = None

def lprint(list):
    node=list
    string=""
    while node:
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

def merge(start1,end1,start2,end2): # To merge [start1,end1) and [start2,end2)

    if not start1:
        return (None,None)

    if not start2:
        return (start1,end1)

    if start1.val<start2.val:
        head=start1
        start1=start1.next
    else:
        head=start2
        start2=start2.next

    cur=head

    while start1!=end1 and start2!=end2:
        if start1.val<start2.val:

            cur.next=start1
            cur=cur.next
            start1=start1.next

        else:
            cur.next=start2
            cur=cur.next
            start2=start2.next


    while start1!=end1:
        cur.next=start1
        start1=start1.next
        cur=cur.next

    while start2!=end2:
        cur.next=start2
        start2=start2.next
        cur=cur.next

    return (head,cur)


def mergesort_bottomup(head):
    if (not head) or (not head.next):
        return head

    size=1

    length=0
    node=head
    while node:
        node=node.next
        length+=1

    def Find(node,count):
        i=0
        while node and i<count:
            node=node.next
            i+=1
        return node

    while size<length:
        i=0
        last=ListNode(0)
        last.next=head
        # to initialize and prepare for the segment merge sort; finish the connection
        while True:
           # find start1=i, end1=i+size, end2=i+size*2 .The idea is separate [start,end) as a segment to do merge, and
           # use last to connect to the next segment. Because we need to connect between segments.

            start1=last.next
            end1=Find(start1,size)

            if end1:
                start2=end1
            else:
                break

            end2=Find(start2,size)

            (seghead,segend)=merge(start1,end1,start2,end2)
            if i==0:
                head=seghead
            last.next=seghead
            last=segend
            last.next=end2

            i=i+2*size

        size=size*2

    return head



def test_main(list1,list2):
    if (not list1) or (not list2):
        return
    L1=prepareList(list1)
    L2=prepareList(list2)

    lprint(L1)
    lprint(L2)

    start1=L1
    while L1.next:
        L1=L1.next

    end1=L1

    start2=L2

    while L2.next:
        L2=L2.next

    end2=L2


    (head,end)=merge(start1,None,start2,None)

    lprint(head)

    print(head.val)
    print(end.val)

thead=prepareList([6,7,8,10,12,14,16,-10,11,123,304,1,2,3,4,5])

result=mergesort_bottomup(thead)

lprint(result)