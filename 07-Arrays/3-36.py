def f(n):
    new_arr=[]
    for row in n:
        for i in row:
            new_arr.append(i)
    return new_arr
print(f([[1, 2, 3, 4, 5],[6, 7, 8, 9, 0]]))
print(f([[2,3],[1,5]]))

