__author__ = 'bozeng'


def largestRectangleArea(height):
    if not height:
        return 0

        # using a queue to keep track of left, closest element smaller than current one; and right smallest element smaller than a given one (that is when it is poped out). and save max in each iteration
    stack=[]
    maxrect=0

    for i in range(len(height)):
        current=height[i]
        while stack:
            if stack[-1][1]>current:
                (index,h,left)=stack.pop()
                maxrect=max(h*(i-index-1)+left,maxrect)
            elif stack[-1][1]==current:
                stack.pop()
            else:
                break
        if stack:
            stack.append((i,current,current*(i-(stack[-1])[0])))
        else:
            stack.append((i,current,current*(i+1)))

    while stack:
        (index,h,left)=stack.pop()
        print((index,h,left))
        maxrect=max(h*(len(height)-index-1)+left,maxrect)

    return maxrect


print(largestRectangleArea([2,1,5,6,2,3]))