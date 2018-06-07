# JTSK-350111
# a3 p6.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

ch = input('Enter a character: ')
n = int(input('Enter an integer: '))

# print letters ranging from ch to ch+n in ascii
for i in range(ord(ch), ord(ch)+n+1):
    print(chr(i))