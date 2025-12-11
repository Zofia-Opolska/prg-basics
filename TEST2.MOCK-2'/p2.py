# (p2.py) An array contains at least 3 integers. All numbers in the array are equal except one. Define a function f(arr) 
# that returns a number in the arr array that is different from the other numbers. Example: 
# f([7,7,7,7,7,5,7,7])  5 

def f(arr):
    from collections import Counter
    counts = Counter(arr)
    different_value = [item for item, count in counts.items() if count == 1][0]
    return different_value

print(f([7,7,7,7,7,5,7,7]))
print(f([5,7,7]))
print(f([7,7,7,7,7,5]))