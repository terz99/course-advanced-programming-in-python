# JTSK-350111
# a2 p4.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (9/5)*celsius + 32
print("The temperature in fahrenheit is {:f}F".format(fahrenheit))

if fahrenheit < 32:
    print("cold")
elif fahrenheit > 104:
    print("hot")