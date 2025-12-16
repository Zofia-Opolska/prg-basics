# returns True when the sum of the values in each row of the array is equal to the sum of the values in the corresponding column 
# and False otherwise. Example: 
# f([[3,7,2],
#   [4,2,5],
#   [5,2,1]])  True 
# f([[3,7,2],
#    [4,2,5],
#    [9,2,1]])  False 

def f(arr):
    i=0
    for row in arr:
        if sum(row)==arr[0][i]+arr[1][i]+arr[2][i]:
            i+=1
        else:
            return False
    return True

print(f(([[3,7,2],[4,2,5],[5,2,1]])))
print(f([[3,7,2],[4,2,5],[9,2,1]]))