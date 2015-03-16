__author__ = 'bozeng'

def make_change(amount, coins):

    if not coins:
        return None
    smallest = min(coins)
    rest = remove_one(coins, smallest)
    "*** YOUR CODE HERE ***"

    if amount == 0:
        return None

    if amount - smallest < 0:
        return None

    if amount - smallest ==0:
        return [smallest]

    trial1=make_change(amount - smallest, rest)

    if trial1 :
        result=[smallest]
        result.extend(trial1[:])
        return result

    without=dict(coins)
    without.pop(smallest)
    trial2=make_change(amount, without)

    if trial2 :
        result=[]
        result.extend(trial2[:])
        return result

    return None

def remove_one(coins, coin):

    copy = dict(coins)
    count = copy.pop(coin) - 1
    if count:
        copy[coin] = count
    return copy


print(make_change(25, {2: 2, 3: 2, 4: 3, 5: 1, 8 : 1}))