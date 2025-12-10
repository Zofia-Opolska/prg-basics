arr=[[0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0]]
      
for i in range(5):        # rows
    for j in range(5):    # columns
        arr[i][j] = (i+1) * (j+1)

# Print the array
for row in arr:
    for value in row:
        print(value, end=" ")
    print()