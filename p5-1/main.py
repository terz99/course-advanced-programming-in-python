# JTSK-350111
# a5 p1.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

fRead = open('input.txt', 'r')
product = 1
for line in fRead:
    line = line.strip();
    product = product*ord(line)
fRead.close()
fWrite = open('output.txt', 'w')
fWrite.write(str(product))
fWrite.close()