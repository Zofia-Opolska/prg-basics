# (p10.py) A two-dimensional array contains different integer numbers. Define a function f(array) that returns True if 
# the row and column numbers for the smallest value in the array are equal, and False otherwise. Example: 
# f([[7,8],[5,3],[9,4]])  True     
# # 3, row 1, col 1 
# f([[7,8,5,3],[9,4,2,6]])  False  # 2, row 1, col 2 

def f(array): 
    smallest_value = float('inf')
    a=-1
    b=-1
    for row in range(len(array)):
        for i in range(len(array[row])):
            if array[row][i] < smallest_value:
                smallest_value = array[row][i]
                b = i
                a = row
    return a == b

print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))