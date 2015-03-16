__author__ = 'bozeng'

 # return list of all valid partitioning

 # your favorite way if back-tracking


 # but more efficienty way is DP


def palinpart(string):
    if not string:
         return []

     #do it DP. ( because each solution can be recursively defined by the start part of the solution, i.e. the first palindrome.e
     # the set of all partitions can be defined by the first palindrome recursively. (back tracking is not reusing results)

    DPMatrix=[[] for _ in range(len(string)+1)]

    DPMatrix[0]=[]
    DPMatrix[1]=[[string[0]]]

    PalinMatrix=[[False for _ in range(len(string))] for __ in range(len(string)) ]

    for size in range(len(string)):
        for start in range(len(string)-size):
            if size==0:
                PalinMatrix[start][start+size]=True
            elif size==1:
                PalinMatrix[start][start+size]=True if string[start]==string[start+size] else False

            else:
                PalinMatrix[start][start+size]=PalinMatrix[start+1][start+size-1] if string[start]==string[start+size] else False


    for i in range(2,len(string)+1):
        for j in range(i):
            if PalinMatrix[j][i-1]:
                if j==0:
                    DPMatrix[i].append([string[j:i]])
                for each in DPMatrix[j]:
                    temp=each[:]
                    temp.append(string[j:i])
                    DPMatrix[i].append(temp)


    return DPMatrix[len(string)]


print(palinpart("aabaass"))