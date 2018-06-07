# JTSK-350111
# a6 p7.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

from turtle import Turtle

def moveforward(t):
    t.forward(10)
def turnleft(t):
    t.left(15)
def turnright(t):
    t.right(15)
def goup(t):
    t.up()
def godown(t):
    t.down()

jumpTable = {}
jumpTable["F"] = moveforward
jumpTable["L"] = turnleft
jumpTable["R"] = turnright
jumpTable["U"] = goup
jumpTable["D"] = godown 

t = Turtle()
t.screen.setup(width = 600, height = 600)

while True:
    op = str(input("Enter string to execute: "))
    if op == "":
        break
    for letter in op:
        exists = jumpTable.get(letter, None)
        if exists != None:
            jumpTable[letter](t)
