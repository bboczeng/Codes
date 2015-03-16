__author__ = 'bozeng'


""" only mark the solution until you find the solution """


def permutate(string):

    tolist=[]
    for char in string:
        tolist.append(char)

    def swap(list,i,j):
        temp=list[i]
        list[i]=list[j]
        list[j]=temp
    result=[]

    def helper(list,step):
        if step==len(list)-1:
            result.append("".join(list))

        for i in range(step,len(list)):
            swap(list,step,i)
            helper(list,step+1)
            swap(list,step,i)

    helper(tolist,0)
    return result

print(permutate("56789"))