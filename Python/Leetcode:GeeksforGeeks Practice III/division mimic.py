__author__ = 'bozeng'


def division(nom,denom):
    if nom==0:
        return "0"
    result=""
    if (nom<0) ^ (denom<0):
        result+="-"

    nom=abs(nom)
    denom=abs(denom)

    result+=str(nom//denom)


    r=nom%denom

    if r==0:
        return result

    result+="."

    history={}
    while r:

        if r in history:
            result=result[0:history[r]]+"("+result[history[r]:]+")"
            break

        history[r]=len(result)
        result+=str((r*10)//denom)
        r=(r*10)%denom

    return result

print(division(-120553,100))