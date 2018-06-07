# 350111
# a4 p6.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

import random

random.seed()
minval = 1
maxval = 50
r = random.randint(minval, maxval)
counter = 0
while True:
    counter += 1
    guess = int(input("Enter your guess: "))
    if guess == r:
        print("You got it!")
        break
    elif guess < r:
        print("Your #{:d} guess is too small!".format(counter))
    else:
        print("Your #{:d} guess is too high!".format(counter))
print("Bye")