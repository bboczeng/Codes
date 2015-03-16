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

def sortList(head):
        if not head:
            return None

        # do quick sort version

        def swap(node1,node2):
            temp=node1.val
            node1.val=node2.val
            node2.val=temp

        length=0
        node=head
        while node:
            length+=1
            node=node.next

        if length==1:
            return head

        def qsort(lhead, length):
            if not lhead:
                return
            if length<=1:
                return
            pivot=lhead
            end=lhead
            count=0

            while count<length-1:
                if count==(length-1)//2:
                    pivot=end
                end=end.next
                count+=1

            swap(pivot,end)


            node=lhead
            pivot=lhead
            count=0
            while count<length:
                if node.val>=end.val:
                    pivot=node
                    break
                node=node.next
                count+=1

            node=pivot.next
            marker=count
            count+=1
            print(marker)

            while count<length-1:
                if node.val<end.val:
                    swap(node,pivot)
                    pivot=pivot.next
                    marker+=1
                node=node.next
                count+=1

            swap(end,pivot)

            qsort(lhead, marker)
            qsort(pivot.next, length-marker-1)

        qsort(head,length)
        return head

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



test=prepareList([10,1,2,3,4,6,5,10,2,3,43,0,34534353,45,56564,34535,2,2134131,12432,45,-102031,-1231,-43,5,-65])

lprint(test)

sortList(test)

lprint(test)


