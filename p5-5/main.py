# JTSK-350111
# a5 p5.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

def add(lst, val):
    
    """ This function adds val to each element in lst """

    newList = lst[:]
    for i in range(len(newList)):
        newList[i] += val
    return newList

def multiply(lst, val):

    """ This function multiplies each element of lst with val """

    newList = lst[:]
    for i in range(len(newList)):
        newList[i] += val
    return newList

numOfElems = int(input("Enter the number of elements: "))
# write the numbers in separate lines
lst = []
for _ in range(numOfElems):
    lst.append(float(input()))

lst1 = add(lst, 1.5)
lst2 = multiply(lst, 5)
print(lst)
print(lst1)
print(lst2)
