# 350111
# a4 p7.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

string = input("Enter a string:\n")

# basically, what these two nested for loops do is
# writing string on the diagonal of len(string) X len(string) matrix
for i in range(len(string)):
    for j in range(len(string)):
        if i == j:
            print(string[i])
            break
        else:
            print(' ', end='')