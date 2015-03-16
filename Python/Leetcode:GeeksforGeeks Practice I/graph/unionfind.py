__author__ = 'bozeng'


class ufNode:
    def __init__(self,value,parent):
        self.value=value
        self.parent=parent
        self.rank=1


class unionFindSet:
    def __init__(self,size):
        self.ufArray=[None]*size
        self.maxSize=size
        self.count=0

    def create(self,alist):
        assert type(alist) is list or type(alist) is tuple or type(alist) is str, "input not iterable"
        if len(alist)>self.maxSize:
            print("can not create, size exceeds limit")
            return

        for i in range(len(alist)):
            self.ufArray[i]=ufNode(alist[i],i)
            self.count+=1

    def add(self,value):
        if self.count==self.maxSize:
            print("exceeds size limit")
            return

        self.ufArray[self.count]=ufNode(value,self.count)  # parent pointing to himself

        self.count+=1



    def find(self,x):
        # assume value is stored in its numerical index
        if self.ufArray[x]==None or x>=self.maxSize or x<0:
            print("element not in array")
            return -1
        if self.ufArray[x].parent==x:
            return x
        else:
            self.ufArray[x].parent=self.find(self.ufArray[x].parent)
            return self.ufArray[x].parent


    def union(self,x,y):
        if self.ufArray[x]==None or x>=self.maxSize or x<0 or self.ufArray[y]==None or y>=self.maxSize or y<0:
            print("element not in array")
            return -1

        parentx=self.find(x)
        parenty=self.find(y)

        if parentx==parenty:
            return

        else:
            if self.ufArray[parentx].rank<self.ufArray[parenty].rank:
                self.ufArray[parentx].parent=parenty
            elif self.ufArray[parentx].rank>self.ufArray[parenty].rank:
                self.ufArray[parenty].parent=parentx
            else:
                self.ufArray[parentx].parent=parenty
                self.ufArray[parenty].rank+=1





uf1=unionFindSet(11)
uf1.create([0,1,2,3,4,5,6,7,8,9,10])

print(uf1.find(3))

uf1.union(1,2)
uf1.union(2,3)

print(uf1.find(3))

uf1.union(5,6)
uf1.union(5,9)
uf1.union(8,10)
uf1.union(8,9)

print("test")

for i in range(uf1.count):
    print(uf1.find(i))



