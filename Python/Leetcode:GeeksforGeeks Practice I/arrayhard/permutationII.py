__author__ = 'bozeng'



def permutationii(array):
    if not array:
        return []


    def swap(i,j):
        temp=array[i]
        array[i]=array[j]
        array[j]=temp

    def backtracking(result,index):

        if index==len(array):
            result.append(array[:])
            return

        for i in range(index,len(array)):
            swap(index,i)
            backtracking(result,index+1)
            swap(index,i)


    result=[]

    backtracking(result,0)

    dict={}

    for each in result:
        if tuple(each) not in dict:
            dict[tuple(each)]=1

    result=[]
    for each in dict:
        result.append(list(each))

    return result

print(permutationii([1,1,1,1,1,3]))


def permutationiibetter(array):
    if not array:
        return []

    array.sort()
    def swap(i,j):
        temp=array[i]
        array[i]=array[j]
        array[j]=temp

    def backtracking(result,index):

        if index==len(array):
            result.append(array[:])
            return

        for i in range(index,len(array)):
            if i==index or (array[i]!=array[i-1] and array[i]!=array[index]):
                swap(index,i)
                backtracking(result,index+1)
                swap(index,i)


    result=[]

    backtracking(result,0)


    return result


def permutationwithdupII(num):
    if not num:
        return []
    num.sort()
    ret = [[]]
    for n in num:
        new_ret = []
        l = len(ret[-1])
        for seq in ret:
            for i in range(l, -1, -1):
                if i < l and seq[i] == n:
                    break
                new_ret.append(seq[:i] + [n] + seq[i:])
        ret = new_ret
    return ret

print(permutationiibetter([0,1,0,0,9]))
print(permutationwithdupII([0,1,0,0,9]))