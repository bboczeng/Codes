__author__ = 'bozeng'

## this code implements a hashtable.

class Item:
        def __init__(self, key, value):
            self.key=key
            self.value=value

## do it using linear probing and two lists (for easier retrieval of keys and values ). Use Open addressing. Should support resizing

class hashTable:


    def __init__(self):
        self.arraysize=8
        self.itemsize=0
        self.itemarray=[-1]*self.arraysize


    def update(self,newsize):

        oldarray=self.itemarray
        oldsize=self.arraysize

        self.arraysize=newsize

        self.itemarray=[-1]*newsize

        self.itemsize=0

        for i in range(oldsize):
            if oldarray[i]!=-1:
                self.put(oldarray[i].key,oldarray[i].value)


    def put(self,key,value):

        if (self.itemsize+1)*3>=2*self.arraysize:
            self.update(self.arraysize*2)

        position=self.hashing(key)
        if self.itemarray[position]==-1:
            self.itemarray[position]=Item(key,value)
            self.itemsize=1+self.itemsize
            return
        else:
            nextposition=position
            count=1
            while True:
                if self.itemarray[nextposition]==-1:
                    self.itemarray[nextposition]=Item(key,value)
                    self.itemsize=1+self.itemsize
                    return
                elif self.itemarray[nextposition].key==key:
                    self.itemarray[nextposition].value=value
                    return

                nextposition=self.rehash(nextposition,count)
                count=count+1





    def rehash(self,hashvalue,count):

        return (hashvalue+count**2)%self.arraysize

    def hashing(self,key):

        return  hash(key)%(self.arraysize-1)


    def get(self,key):

        position=self.hashing(key)
        if self.itemarray[position]==-1:
            return None
        else:
            nextposition=position
            count=1
            while True:
                if self.itemarray[nextposition]==-1:
                    return None
                elif self.itemarray[nextposition].key==key:
                    return self.itemarray[position].value

                nextposition=self.rehash(nextposition,count)
                count=count+1


    def __getitem__(self,key):

        return self.get(key)

    def __setitem__(self,key,value):

        return self.put(key,value)

    def __len__(self):
        return self.itemsize

    def __contains__(self, key):
        return self.get(key)!=None

    def __delitem__(self, key):

        position=self.hashing(key)
        if self.itemarray[position]==-1:
            raise KeyError("%s does not exist" % key)
        else:
            nextposition=position
            count=1
            while True:
                if self.itemarray[nextposition]==-1:
                    raise KeyError("%s does not exist" % key)
                elif self.itemarray[nextposition].key==key:
                    self.itemarray[nextposition]=-1
                    self.itemsize=self.itemsize-1
                    return

                nextposition=self.rehash(nextposition,count)
                count=count+1

    def keys(self):

        for i in range(self.arraysize):
            if self.itemarray[i]!=-1:
                yield self.itemarray[i].key


    def values(self):

        for i in range(self.arraysize):
            if self.itemarray[i]!=-1:
                yield self.itemarray[i].value





hs=hashTable()

hs["man"]='adman22'

hs["man2"]='adman'

hs["man3"]='adman'

hs["man4"]='adman'

hs["man5"]='adman'

hs["man6"]='adman'

hs["man7"]='adman'



print(hs.itemarray)

for i in hs.keys():
    print(i in hs)
    print(hs[i])

print(len(hs))