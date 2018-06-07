# JTSK-350111
# a5 p2.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

f = open('numbers.txt', 'r')
total = 0
for line in f:
    line = line.strip()
    total += int(line)
print(total)
f.close()