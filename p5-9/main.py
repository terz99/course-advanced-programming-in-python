# JTSK-350111
# a5 p9.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

def longest_word(lst):

    """ This function returns the longest word in a list of words """
    ret = ''
    for word in lst:
        if len(word) > len(ret):
            ret = word
    return ret

string = input('Enter a string: ')
lst = string.split()
print(len(longest_word(lst)))