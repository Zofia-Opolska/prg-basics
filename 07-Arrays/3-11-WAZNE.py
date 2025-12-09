'''Create a program that sorts elements of an array containing integer numbers. 
Apply the Bubble Sort sorting algorithm. 
Define a function bubblesort(array) that returns the sorted array. 
Try to sort and print any three arrays.'''

def bs(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
print(bs([4,36,12,28,9,44,5]))
  