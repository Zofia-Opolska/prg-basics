arr = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_value = arr[0][0]
max_value = arr[0][0]

min_pos = (0, 0)
max_pos = (0, 0)

for r in range(len(arr)):
    for c in range(len(arr[r])):
        value = arr[r][c]

        if value < min_value:
            min_value = value
            min_pos = (r, c)

        if value > max_value:
            max_value = value
            max_pos = (r, c)

# Print results
print("Smallest value:", min_value, "at row", min_pos[0], "column", min_pos[1])
print("Largest value :", max_value, "at row", max_pos[0], "column", max_pos[1])
