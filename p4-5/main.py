# 350111
# a4 p5.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

from math import pi

def get_area(radius):
    return (4*pi*(radius**3))/3

r = float(input("Enter the radius of the sphere: "))
area = get_area(r)
print("The area of a sphere with radius {:f} is {:f}".format(r, area))