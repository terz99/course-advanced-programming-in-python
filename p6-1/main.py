# JTSK-350111
# a6 p1.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

from turtle import *

length = int(input("Enter the length of the square: "))

t = Turtle()
t.screen.setup(width=600, height=600)

# move the turtle to the right top corner
t.up()
t.setheading(90)
t.forward(length/2)
t.left(90)
t.forward(length/2)
t.setheading(0)

# draw square
t.down()
for _ in range(4):
    t.forward(length)
    t.right(90)