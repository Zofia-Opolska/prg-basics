# The following array represents a square matrix and contains values:

# [
#    [0,0,0],
#    [0,0,0],
#    [0,0,0]
# ]
# Create a program that replaces the values of the main diagonal with 1. Use a loop statement. Print the modified array. Sample result:

# 1 0 0
# 0 1 0
# 0 0 1

array=[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

def f(array):
    i=0
    for row in array:
        row[i]=1
        i+=1
    return array
print(f(array=[[0,0,0],[0,0,0],[0,0,0]]))