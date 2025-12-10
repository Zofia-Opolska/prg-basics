def f(n):
    arr=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        arr.append(row)
    return arr

def f_print(arr):
    for row in arr:
        for i in row:
            print(i, end=" ")
        print()

print(f_print(f(3)))
print(f_print(f(5)))
print(f_print(f(8)))
print(f_print(f(10)))