# JTSK-350111
# a5 p6.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

def histogram(lst):

    """ This function prints a vertical histogram
    from the values of lst """

    for height in lst:
        for _ in range(height):
            print('*', end='')
        print('')

n = int(input('Enter the length of the list: '))
lst = []
# enter numbers in separate lines
for _ in range(n):
    lst.append(int(input()))

histogram(lst)
