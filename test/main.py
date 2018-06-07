import timeit
import random

def merge(arr, x, y ,z):
    arr1 = []
    arr2 = []
    for i in range(x, y+1):
        arr1.append(arr[i])
    for i in range(y+1, z+1):
        arr2.append(arr[i])

    i=0
    j=0
    k=x
    size1 = len(arr1)
    size2 = len(arr2)

    while i<size1 and j<size2:
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1

    while i<size1:
        arr[k]=arr1[i]
        i+=1
        k+=1

    while j<size2:
        arr[k]=arr2[j]
        j+=1
        k+=1

def mergeSort(arr,x,z,k):
    if (z - x + 1) <= k:
        insertionSort(arr, x, z)
    else:
        mid = (x+z)//2
        mergeSort(arr, x, mid, k)
        mergeSort(arr, mid+1, z, k)
        merge(arr, x, mid, z)
        


def insertionSort(arr,x,z):
    # Traverse through 1 to len(arr)
    for i in range(x+1, z+1):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= x and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def main():
    cases=10
    size=150
    k=100
    int_max=2147483647
    f=open("random.txt",'w')
    for i in range(cases):
        array=[0]*size
        k-=10
        f.write(str(k)+"\n")
        for j in range(size):
            array[j]=int(random.randrange(0,int_max))
        start=timeit.timeit()
        mergeSort(array,0,size-1,k)
        end=timeit.timeit()
        f.write(str(end-start)+"\n")


main()