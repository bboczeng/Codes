__author__ = 'bozeng'

"""
returns a boolean indicating if key (string) can be composed of arbitrary concatenation of strings from a given dict.
"""

def arbitraryConcatenate(key,dictionary):

    hashtable={x:1 for x in dictionary}

    # BFS searching, best if len(dictionary)>> len(key)

    stack=[0]

    length=len(key)

    if length==0:
        return False

    while stack:
        position=stack.pop(0)
        if position==length:
            return True

        for i in range(position, length):
            if key[position:i+1] in hashtable:
                stack.append(i+1)




    return False

print(arbitraryConcatenate("tomorrowhappyright!",["tomorrow","happ","happy","right","!"]))

def arbitraryConcatenateDFSbacktracking(key,dictionary):

    # DFS backtracking searching, best if len(dictionary)<< len(key)
    if not key:
        return False

    length=len(key)


    def backtracking(position):
        if position==length:
            return True

        for eachitem in dictionary:
            itemlength=len(eachitem)
            if itemlength <= length-position and key[position:position+itemlength]==eachitem:
                if backtracking(position+itemlength):
                    return True

        return False

    if backtracking(0):
        return True

    return False

print(arbitraryConcatenateDFSbacktracking("tomorrowhappyright!",["tomorrow","happ","happy","right","!"]))


def arbitraryConcatenateDP(key,dictionary):
    # its optimal case is actually much worse than DFS and BFS searches. but it has a best worst-case bound.
    if not key:
        return False

    hashtable={x:1 for x in dictionary}

    DPresult=[[False]*len(key) for x in key]




    for sublength in range(len(key)):
        for i in range(len(key)-sublength):
            if key[i:i+sublength+1] in hashtable:
                DPresult[i][i+sublength]=True
                continue
            for j in range(i+1,i+sublength+1):
                if DPresult[i][j-1] and key[j:i+sublength+1] in hashtable:
                    DPresult[i][i+sublength]=True
                    break

    return DPresult[0][len(key)-1]



print(arbitraryConcatenateDP("tomorrowhappyright!",["tomorrow","happ","happy","right","!"]))