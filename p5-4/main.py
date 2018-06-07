# JTSK-350111
# a5 p4.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

fileName = input('Enter the name of the file: ')
fileRead = open(fileName, 'r')
fileWrite = open('copy.txt', 'w')
for line in fileRead:
    fileWrite.write(line)
fileRead.close()
fileWrite.close()