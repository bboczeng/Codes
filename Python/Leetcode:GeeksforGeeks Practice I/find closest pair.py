__author__ = 'bozeng'


def closest(a,sum):
    if not a:
        return

    start=0
    end=len(a)-1

    difference=abs(sum-(a[end]+a[start]))
    found1=start
    found2=end

    while start<end:
        print(start,end,difference)
        if abs(sum-(a[end]+a[start]))<difference:
            difference=abs(sum-(a[end]+a[start]))
            found1=start
            found2=end

        if sum-(a[end]+a[start])<0:
            end=end-1

        elif sum-(a[end]+a[start])>0:
            start=start+1

        else:
            difference=0
            found1=start
            found2=end
            break

    return difference, a[found1],a[found2]


print(closest([1,3,4,7,10],8))


