# JTSK-350111
# a3 p7.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

# input the character ch and check its validity
ch = input('Enter a character: ')
while not ('A' <= ch <= 'Z'):
    ch = input('Invalid character input. Try again: ')

# input integer n and check its validity
n = int(input('Enter an integer: '))
while not (0 <= n <= 32):
    n = int(input('Invalid integer input. Try again: '))

# print letters ranging from ch to ch+n in ascii
for i in range(ord(ch), ord(ch)+n+1):
    print(chr(i))