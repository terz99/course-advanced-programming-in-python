# JTSK-350111
# a5 p3.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

fileName = input("Enter the name of the file: ")
file = open(fileName, 'r')
counter = 1
for line in file:
    line = line.strip().split()
    print('On line {:d} there are {:d} words'.format(counter, len(line)))
    counter += 1

