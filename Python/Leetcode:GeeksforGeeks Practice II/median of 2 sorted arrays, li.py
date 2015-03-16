__author__ = 'bozeng'
class Solution:
    # @return a float
    def findMedianSortedArrays(self,a1,a2):
        n1=len(a1)
        n2=len(a2)

        def order_statistic(m):  #find the mth smallest number in the two arrays, obviously 1<=m<=n1+n2
            i1=i2=0
            #In the following while loop, I'll repetitively find the mth smallest number among a1[i1:] and a2[i2:]. For any positive m1 and m2 such that m1+m2<=m, we can illiminate either a1[i1:i1+m1] or a2[i2:i2+m2] by comparing the last elements in the two subarrays. please be aware that m gets updated in each iteration
            while i1<n1 and i2<n2:  #index going out of bound means we have only one array left to investigate
                if m==1:
                    return min(a1[i1],a2[i2])
                #choose m1 and m2 to be about half of m but also make sure the two subarrays don't go out of bound
                m1=m//2
                m2=m-m1
                m1=min(m1,n1-i1)
                m2=min(m2,n2-i2)
                if a1[i1+m1-1]>a2[i2+m2-1]:  #illiminate a2[i2:i2+m2]
                    i2+=m2
                    m-=m2
                else:   #illiminate a1[i:i1+m1]
                    i1+=m1
                    m-=m1
            # the following two lines are for the case where we have only one array left
            if i1==n1: return a2[i2+m-1]
            else: return a1[i1+m-1]

        m, n_mod=divmod(n1+n2,2)
        if n_mod: return order_statistic(m+1)
        else: return float(order_statistic(m)+order_statistic(m+1))/2