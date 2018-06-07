# JTSK-350111
# a6 p2.py
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

length = int(input("Enter the length of the squares' side: "))

t = Turtle()
t.screen.setup(width=700, height=700)
# move the cursor to the upper right corner
moveToStart(t, fixedLength)

# draw the big square with fixedLength
drawSquare(t, fixedLength)

t.pencolor("green")
# draw small squares
for _ in range(4):
    drawSquare(t, length)
    t.up()
    t.forward(fixedLength)
    t.right(90)
    t.down()