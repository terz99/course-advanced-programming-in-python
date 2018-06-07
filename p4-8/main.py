# 350111
# a4 p8.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

# function which returns the number of vowels in a string
# params:
#   s -> string
# return:
#   int -> the number of vowels in s
def count_vowels(s):

    res = 0

    # put all characters in lowercase so we don't check for uppercase letters
    s = s.lower()
    for letter in s:
        if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
            res += 1
    
    return res

string = input("Enter string (or enter to quit):\n")

while string != "":
    print("This string has {:d} vowels".format(count_vowels(string)))
    string = input("Enter a string (or enter to quit):\n")
