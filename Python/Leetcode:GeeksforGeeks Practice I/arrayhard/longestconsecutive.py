__author__ = 'bozeng'


# this longest consecutive doesn't require order. So basically it requires
# A hash storage technique with correct updating. (i was thinking of union-find, but not very necessary)
# SIZE update can be achieved by observing the structure of merges sets. : only need to update the edge elements.
# also their position can be found using existing information


# algorithm design. this is a very good question.

def longestConsecutive(num):
    if not num:
        return 0

    history={}

    maxsize=0

    for each in num:
        if each in history:
            continue
        # this means each must be an edge.
        leftsize=0
        rightsize=0
        if each-1 in history:
            leftsize=history[each-1]

        if each+1 in history:
            rightsize=history[each+1]

        # and they are not connected due to the absence of each.

        totalsize=leftsize+rightsize+1

        history[each]=totalsize # but this is not very useful, since others will check edge numbers of this
        # consecutive list. Only  useful if totalsize=1

        # find the edge numbers
        history[each-leftsize]=totalsize  # this is the trick. (fast location)
        history[each+rightsize]=totalsize
        maxsize=max(maxsize,totalsize)

    return maxsize



print(longestConsecutive([100,4,200,1,3,2,5,0,7,8,9,10,11,12,13,14]))


