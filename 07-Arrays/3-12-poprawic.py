# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

arr=[2,3,2,5,8,1,9,8]
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)