# JTSK-350111
# a6 p3.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

from turtle import *

fixedLength = 600

def moveToStart(t, length):

    """ This function moves the turtle to the 
    right upper corner of the squares """

    t.up()
    t.setheading(90)
    t.forward(length/2)
    t.left(90)
    t.forward(length/2)
    t.setheading(0)
    t.down()

def drawSquare(t, length):

    """ This function draws a square with length length 
    starting from the position where the turtle currently is """

    for _ in range(4):
        t.forward(length)
        t.right(90)

radius = int(input("Enter the radius of the circles: "))

t = Turtle()
t.screen.setup(width = 700, height = 700)
moveToStart(t, fixedLength)
drawSquare(t, fixedLength)

# hardcoding the drawings of the circle 
# because i could not find an algorithm
t.pencolor("orange")
t.up()
t.right(90)
t.forward(2*radius)
t.left(90)
t.forward(radius)
t.down()
t.circle(radius)

t.up()
t.forward(fixedLength-2*radius)
t.down()
t.circle(radius)

t.up()
t.right(90)
t.forward(fixedLength-4*radius)
t.right(90)
t.down()
t.circle(radius)

t.up()
t.forward(fixedLength-2*radius)
t.down()
t.circle(radius)

