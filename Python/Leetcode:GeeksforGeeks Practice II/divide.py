__author__ = 'bozeng'

def divide(dividend, divisor):
        res=[0]
        if dividend==0:
            return 0
        if dividend<0:
            flag=-1
            tdividend=0-dividend
        else:
            flag=1
            tdividend=dividend

        def recursivediv(divd,divs,res):
            tempc=1
            tempd=divs
            while divd-tempd>=0:
                tempc=tempc<<1
                tempd=tempd<<1
            tempc=tempc>>1
            if tempc==0:
                return
            else:
                tempd=tempd>>1
            res[0]=res[0]+tempc
            if divd-tempd==0:
                return
            else:
                recursivediv(divd-tempd,divs,res)

        recursivediv(tdividend,divisor,res)
        if flag==1:
            return res[0]
        else:
            return 0-res[0]


print(divide(2,3))