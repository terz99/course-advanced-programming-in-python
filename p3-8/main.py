# JTSK-350111
# a3 p8.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

count = 0 # the number of numbers entered
total = 0 # sum 
while count < 10: # at most 10 numbers can be entered
    n = int(input('Enter an integer (or -9 to exit): '))
    if n == -9:
        break
    total += n
    count += 1

if count == 0:
    # if -9 is entered directly, then there are no numbers
    print('There are no numbers.')
else:
    print('The average of all the numbers is {:f}'.format(total/count))