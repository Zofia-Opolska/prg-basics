# (p10.py) A two-dimensional array contains different integer numbers. Define a function f(array) that returns True if 
# the row and column numbers for the smallest value in the array are equal, and False otherwise. Example: 
# f([[7,8],[5,3],[9,4]])  True     
# # 3, row 1, col 1 
# f([[7,8,5,3],[9,4,2,6]])  False  # 2, row 1, col 2 

def f(array): 

    row_counter=-1
    column_counter=-1
    main_min= float('inf')
    main_min_2=float('inf')
    for row in array:
        if min(row)<main_min:
            main_min=min(row)
            row_counter+=1
    for column in str(array):
        if column not in ['[',']',',']:
            column_counter+=1
            if column == main_min:
                return column_counter
    if row_counter==column_counter:
        return True
    else:
        return False


# [[7,8],
# [5,3],
# [9,4]])

# [[7,8,5,3],
# [9,4,2,6]])

print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))

