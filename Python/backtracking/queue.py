__author__ = 'bozeng'


# N Queue:

def queue(n,P,R):
    if n==0:
        return 0

    Array=list(x for x in range(n))

    global count
    count=0

    def swap(list,i,j):
        temp=list[i]
        list[i]=list[j]
        list[j]=temp

    def backtracking(lmax,length,pnow):

        if length==n:
            if pnow==P:
                rightmax=-1
                rcount=0
                for i in range(n):
                    if Array[n-i-1]>rightmax:
                        rightmax=Array[n-i-1]
                        rcount=1+rcount
                if rcount==R:
                    global count
                    count=count+1
                    return
            else:
                return
        elif pnow>P:
            return

        else:
            for i in range(length,n):
                swap(Array,length,i)

                if Array[length]>lmax:
                    backtracking(Array[length],length+1,pnow+1)
                else:
                    backtracking(lmax,length+1,pnow)
                swap(Array,length,i)
        return

    backtracking(-1,0,0)
    print(count)

queue(8,4,1)





