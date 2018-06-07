# JTSK-350111
# a6 p5.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

from turtle import (Turtle, done)
from math import pi

radius = 100
num_of_petals = 24
small_radius = 50
shift_angle = 180-((num_of_petals-2)*180)/num_of_petals
shift_distance = 2*radius*pi/num_of_petals

t = Turtle()
t.screen.setup(width = 700, height = 700)

# moving the turtle to the starting point
t.up()
t.setheading(180)
t.forward(radius)
t.down()

# draw big cricle
t.color("yellow")
t.begin_fill()
t.setheading(270)
t.circle(radius)
t.end_fill()
t.setheading(0)

# draw leaves
t.color("red", "pink")
t.begin_fill()
for _ in range(num_of_petals):
    t.circle(small_radius)
    t.up()
    t.right(90)
    t.left(shift_angle)
    t.forward(shift_distance)
    t.left(90)
    t.down()
    
t.end_fill()

done()