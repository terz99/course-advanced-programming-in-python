# JTSK-350111
# a2 p5.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

mins = int(input("Enter minutes: "))

if mins < 0:
    print("Invalid output")
else:
    hours = mins//60
    mins -= hours*60
    print("{:d} hours and {:d} minutes.".format(hours, mins))