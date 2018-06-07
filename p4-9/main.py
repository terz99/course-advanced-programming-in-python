# 350111
# a4 p9.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

s = input("Enter a string: ")

a, b = int(input("Enter first index (0-based): ")), int(input("Enter second index (0-based): "))
while not (0 <= a < len(s) and 0 <= b < len(s)):
    # invalid input, try again
    print("Invalid indicies. Try again!")
    a, b = int(input("Enter first index (0-based): ")), int(input("Enter second index (0-based): "))

# add +1 to b to include the character at position b as well
print(s[a:b+1])