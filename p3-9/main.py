# JTSK-350111
# a3 p9.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

def print_rectangle(n, m, c):
    for _ in range(0, n):
        for _ in range(0, m):
            print(c, end='')
        print('') # print endline

n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))
c = input('Enter a character: ')

print_rectangle(n, m, c)
