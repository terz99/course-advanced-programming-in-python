# JTSK-350111
# a3 p4.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

n = int(input('Enter an integer: '))

for i in range(1, n+1):
    if(i == 1):
        print('{:d} minute = {:d} seconds'.format(i, i*60))
    else:
        print('{:d} minutes = {:d} seconds'.format(i, i*60))