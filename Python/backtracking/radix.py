__author__ = 'bozeng'

def radixsort():


    def numeric_compare(x, y):
        num1=x+y
        num2=y+x

        return num1>num2

    result=["121","12"]

    result.sort(key=numeric_compare)

    print(result)

radixsort()