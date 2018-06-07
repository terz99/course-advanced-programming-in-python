# JTSK-350111
# a3 p10.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

def print_frame(n, m, c):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1:
                # check if it's the upper or lower edge of the frame
                print(c, end='')
            elif j == 0 or j == m-1:
                # check if it's the left or right edge of the frame
                print(c, end='')
            else:
                # otherwise it's void
                print(' ', end='')
        print('') # print endline

n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns'))
c = input('Enter a character: ')

print_frame(n, m, c)