__author__ = 'bozeng'

""" reverse a string can not be done with string.reverse() because, a string is not mutable and reverse() is done in place!"""

""" the way to make a copy of reversed string is string[::-1] """

def convertToTitle(num):
    string = ''
    number = num - 1
    while True:
        r, q = number % 26, number // 26
        string += chr(r + ord('A'))
        number = q - 1
        if number < 0:
            break
    return string[::-1]

print(convertToTitle(28))