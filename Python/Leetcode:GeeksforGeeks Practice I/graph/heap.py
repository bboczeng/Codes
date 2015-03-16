__author__ = 'bozeng'

# a binary implementation of heap. Familiarze with other time complexities of heap.
# check

class hpNode:
    def __init__(self,data,value):
        self.value=value
        self.data=data

class heap:
    def __init__(self,size):
        self.hpArray=[None]*size
        self.maxSize=size
        self.count=0

    def heapify(self,alist):
        assert type(alist) is list or type(alist) is tuple or type(alist) is str, "input not iterable"
        if len(alist)>self.maxSize:
            print("can not heapify, size exceeds limit")
            return

        for i in range(len(alist)):
            self.hpArray[i]=hpNode(alist[i],alist[i])
            self.count+=1

        for i in range(self.count-1,-1,-1):
            self.__siftdown(i)

    def __swap(self,pos1,pos2):
        assert pos1>=0 and pos2>=0 and pos1<self.count and pos2<self.count, "out of bounds"
        temp=self.hpArray[pos1]
        self.hpArray[pos1]=self.hpArray[pos2]
        self.hpArray[pos2]=temp

    def __siftdown(self,position):
        assert position>=0 and position<self.count, "out of bounds"
        while True:
            left=self.__childrenleft(position)
            right=self.__childrenright(position)
            if left==-1:
                break
            if right==-1 or self.hpArray[left].value<self.hpArray[right].value:
                if self.hpArray[position].value>self.hpArray[left].value:
                    self.__swap(left,position)
                    position=left
                else:
                    break
            else:
                if self.hpArray[position].value>self.hpArray[right].value:
                    self.__swap(right,position)
                    position=right
                else:
                    break


    def __siftup(self,position):
        assert position>=0 and position<self.count, "out of bounds"
        while True:
            parent=self.__parent(position)
            if parent==-1:
                break

            if self.hpArray[parent].value>self.hpArray[position].value:
                self.__swap(parent,position)
                position=parent
            else:
                break

    def __parent(self,position):
        assert position>=0, "position can not be negative"
        if position==0:
            return -1
        if position>= self.count:
            return -1

        return (position-1)//2

    def __childrenleft(self,position):
        assert position>=0, "position can not be negative"
        if 2*position+1 >= self.count:
            return -1
        return 2*position+1

    def __childrenright(self,position):
        assert position>=0, "position can not be negative"
        if 2*position+2 >= self.count:
            return -1
        return 2*position+2


    def heappop(self):
        result=self.hpArray[0]
        self.hpArray[0]=self.hpArray[self.count-1]
        self.count-=1
        if self.count>0:
            self.__siftdown(0)
        return result

    def heappush(self,x):
        if self.count==self.maxSize:
            print("heap full")
            return
        self.count+=1
        if type(x) is hpNode:
            self.hpArray[self.count-1]=x
        else:
            self.hpArray[self.count-1]=hpNode(x,x)
        self.__siftup(self.count-1)


hp1=heap(10)

hp1.heapify([100,2,3,4,5,6])

while hp1.count>0:
    print(hp1.heappop().value)

hp1.heappush(100)
hp1.heappush(1000)
hp1.heappush(10)
hp1.heappush(5)
hp1.heappush(70)
hp1.heappush(33)
hp1.heappush(55)
hp1.heappush(13)
hp1.heappush(79)
hp1.heappush(3)


while hp1.count>0:
    print(hp1.heappop().value)


