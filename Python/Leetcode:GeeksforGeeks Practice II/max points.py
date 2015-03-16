__author__ = 'bozeng'

def maxPoints(points):
        length=len(points)
        if length<=2:
            return length
        slopes={}
        lmax=0
        for i in range(length):
            duplicate=1
            for j in range(i+1,length):
                p1x,p1y,p2x,p2y=points[i][0],points[i][1],points[j][0],points[j][1]
                if p1x==p2x and p1y==p2y:
                    duplicate+=1
                    continue
                elif p1x==p2x:
                    if 'inf' in slopes:
                        slopes['inf']+=1
                    else:
                        slopes['inf']=1
                else:
                    slope=(p2y-p1y)/(p2x-p1x)
                    if slope in slopes:
                        slopes[slope]+=1
                    else:
                        slopes[slope]=1
            if len(slopes)==0:
                lmax=max(lmax,duplicate)
            else:
                for keys in slopes:
                    lmax=max(slopes[keys]+duplicate,lmax)
            slopes={}

        return lmax


print(maxPoints([(84,250),(0,0),(1,0),(0,-70),(0,-70),(1,-1),(21,10),(42,90),(-42,-230)]))