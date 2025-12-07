def f(array):
    main_min = float('inf')
    min_row = -1
    min_col = -1

    for i in range(len(array)):          # row index
        for j in range(len(array[i])):   # column index
            if array[i][j] < main_min:
                main_min = array[i][j]
                min_row = i
                min_col = j

    return min_row == min_col

print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))