# JTSK-350111
# a6 p9.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

def scalar_product(v, w):

    """ This function returns the scalar product of vectors v and w """

    ret = 0
    for i in range(len(v)):
        ret = ret + v[i]*w[i]
    return ret

input_list = []
n = int(input("Enter the number of components of both vectors: "))

# please enter the numbers in separate lines
print("Enter components for the first vector:")
for _ in range(n):
    tmp = float(input())
    input_list.append(tmp)
v = tuple(input_list)

input_list.clear()

# please enter numbers in separate lines
print("Enter components for the second vector:")
for _ in range(n):
    tmp = float(input())
    input_list.append(tmp)
w = tuple(input_list)

print("The scalar product of the two vectors is", scalar_product(v, w))

# finding min and max and their indices
merged = v + w
min_val = min(merged)
max_val = max(merged)
print("The minimum value is {} and its index is {}".format(min_val, merged.index(min_val)%n))
print("The maximum value is {} and its index is {}".format(max_val, merged.index(max_val)%n))