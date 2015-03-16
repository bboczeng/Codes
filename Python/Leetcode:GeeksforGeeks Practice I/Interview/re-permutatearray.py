__author__ = 'bozeng'

"""
reassign arr[i] <- arr[arr[i]]

do it in place and with O(n) time

notice this is a permuation.


"""


# this is definitely a trick !!!. remember your current value as well as what your new value should be
# and store them as a single value !!!>

def repermutate(array):
    if not array:
        return []

    if len(array)==1:
        return array

    size=len(array)

    for i in range(size):
        array[i]=array[i]+array[array[i]]*size


    for i in range(size):
        array[i]=(array[i]//size)%size

    return array


print(repermutate([0,1,2,3]))



# your original method works as well! except you can SMARTLY mark visited elements by negating it .


