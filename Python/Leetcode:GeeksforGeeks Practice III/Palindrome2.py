__author__ = 'bozeng'

# check if a number is a palindrome, do its reverse.
def Palindrome(x):
    if x<0:
        return False

    reverse=0
    num=x
    if num<10:
        return True

    while num>0:
        reverse=reverse*10+num%10
        num=num//10

    return reverse==x

print(Palindrome(11211444343434343))