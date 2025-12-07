# (p3.py) A two-dimensional array contains the same number of rows and columns. Define a function f(array2D) that, 
# for the given two-dimensional array array2D, returns True when the sum of the values in each row of the array is 
# equal to the sum of the values in the corresponding column (e.g., the sum of the values in row 3 is equal to the sum 
# of the values in column 3) , and False otherwise. Example: 
# f([[3,7,2],[4,2,5],[5,2,1]])  True 
# f([[3,7,2],[4,2,5],[9,2,1]])  False 

def f(array2D):
    for row in array2D:
        if (array2D[2][0])+(array2D[2][1])+(array2D[2][2]) == (array2D[0][2])+(array2D[1][2])+(array2D[2][2]):
            return True
        elif (array2D[1][0])+(array2D[2][1])+(array2D[2][2]) == (array2D[0][1])+(array2D[1][1])+(array2D[2][1]):
            return True
        elif (array2D[0][0])+(array2D[2][1])+(array2D[2][2]) == (array2D[0][0])+(array2D[1][0])+(array2D[2][0]):
            return True
        else:
            return False
print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))
# [[3,7,2], 0
# [4,2,5], 1
# [5,2,1]] 2