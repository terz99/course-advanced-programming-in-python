# JTSK-350111
# a6 p6.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

from turtle import (Turtle, done)
from math import pi

# this variable is the radius of the circle
radius = 100

def draw_star(t, length):

    """ This method draws a star with length 'length' """

    t.color("yellow", "yellow")
    prev_heading = t.heading()
    t.setheading(0)
    t.begin_fill()
    for _ in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.setheading(prev_heading)

def draw_stars(n):

    """ This method draws n stars around imaginary circle """

    t = Turtle()
    t.screen.setup(width = 700, height = 700)

    if n == 12:
        # not important if statement, omit this
        t.screen.bgcolor("blue")

    # get turtle to starting position on the imaginary circle
    t.up()
    t.setheading(270)
    t.forward(radius)
    t.setheading(0)
    t.down()

    # calculating shift angles and distances
    shift_angle = 180-(n-2)*180/n
    shift_distance = 2*radius*pi/n

    # draw stars
    for _ in range(n):
        draw_star(t, 35)
        t.up()
        t.left(shift_angle)
        t.forward(shift_distance)
        t.down()

    t.hideturtle()


n = int(input("Enter the number of stars (enter 12 to see something interesting): "))

draw_stars(n)
done() # I use this method in order to stop the window screen and see the result of my program
