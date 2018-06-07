# JTSK-350111
# a6 p4.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

from turtle import *

t = Turtle()
t.screen.setup(width = 600, height = 600)
t.width(2)

length = 250

# moving to start
t.up()
t.setheading(180)
t.forward(length/2)
t.setheading(0)
t.down()

# start drawing the star
t.color("blue", "purple")
t.begin_fill()
for _ in range(12):
    t.forward(length)
    t.left(150)
t.end_fill()
# i am using the done() function in order to pause the window
# at the end and see the drawing
done()
