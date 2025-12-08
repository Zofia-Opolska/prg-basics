arr=[-15,8,-31,47,-2,19]
smallest=None
n=0

minimum = arr[0]

# Loop through the array
for i in arr:
    if i < minimum:
        minimum = i

print("Minimum number:", minimum)


