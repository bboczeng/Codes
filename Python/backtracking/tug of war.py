__author__ = 'bozeng'


def tugOfWar(series):
    if len(series)==0:
        return 0

    nitem=len(series)

    sum=0
    for i in series:
        sum+=i


    minDifference=sum
    resultSumLeft=0
    leftsubset=[]
    resultSet=[]

    def backtracking(item,sumleft,numleft):
        nonlocal minDifference
        nonlocal resultSumLeft
        nonlocal leftsubset
        nonlocal resultSet
        nonlocal sum
        if numleft==nitem//2:
            if abs(sum-2*sumleft)<minDifference:
                resultSumLeft=sumleft
                resultSet=leftsubset[:]
            minDifference=min(abs(sum-2*sumleft),minDifference)

            return

        if numleft>nitem//2:
            return

        if item==nitem:
            return

        # if count this item
        leftsubset.append(series[item])
        backtracking(item+1,sumleft+series[item],numleft+1)

        # if not count this item
        leftsubset.pop()
        backtracking(item+1,sumleft,numleft)

    backtracking(0,0,0)

    print(minDifference)
    print(resultSumLeft,sum-resultSumLeft)
    print(resultSet)


tugOfWar([23, 45, -34, 12, 10, 98, -99, 4, 189, -1, 4])