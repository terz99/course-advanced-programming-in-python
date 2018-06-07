# JTSK-350111
# a5 p8.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

def overlapping(list1, list2):

    """ This function returns True if there is an element in
    list1 which is also present in list2, and False otherwise """

    for elem in list1:
        if elem in list2:
            return True;
    return False

list1 = []
list2 = []

# input the first list
while True:
    tmp = int(input('Enter a number (negative to stop): '))
    if tmp < 0:
        break
    list1.append(tmp)

# input the second list
while True:
    tmp = int(input('Enter a number (negative to stop): '))
    if tmp < 0:
        break
    list2.append(tmp)

if overlapping(list1, list2):
    print('The two lists are overlapping.')
else:
    print('The two lists are not overlapping.')