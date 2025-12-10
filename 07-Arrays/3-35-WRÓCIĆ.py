
def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(m[r][c])
        transposed.append(new_row)
    return transposed


def print_matrix(arr):
    for row in arr:
        for value in row:
            print(value, end=" ")
        print()
    print()   

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

C = [
    [5, 6, 7]
]


print("Transpose of A:")
print_matrix(transpose_matrix(A))

print("Transpose of B:")
print_matrix(transpose_matrix(B))

print("Transpose of C:")
print_matrix(transpose_matrix(C))
