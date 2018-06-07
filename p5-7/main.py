# JTSK-350111
# a5 p7.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

lst = []
while True:
    n = int(input('Enter an integer (0 to stop): '))
    if n == 0:
        break
    lst.append(n)

# min returns the minimum element in a list
# max returns the maximum element in a list
print(min(lst))
print(max(lst))