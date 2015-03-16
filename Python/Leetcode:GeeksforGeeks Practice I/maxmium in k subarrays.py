__author__ = 'bozeng'


""" it finds the maximum of all k-consecutive subarrays """

def kmaximum(a,k):
    if len(a)<k:
        return None

    queue=[]

    result=[]

    for i in range(k):
        while (queue and queue[-1]<a[i]):
            queue.pop()

        queue.append(i)

    result.append(a[queue[0]])

    for i in range(k,len(a)):

        while queue and queue[0]<i-k+1: # remove elements that are outside the current k-size window. the largest number of last window may not be outside .
            queue.pop(0)

        while queue and a[queue[-1]]<a[i]: # only keep significant elements after the largest up to now. it means we keep a strickly decreasing queue for
            # numbers after the largest on the current k-size window.
            queue.pop()

        queue.append(i)


        result.append(a[queue[0]])  ## if this invariance is kept, then everytime the top of the queue tells you, the largest number of the current k-size window.

    return result

print(kmaximum([1, 2, 3, 1, 4, 5, 2, 3, 6],3))





