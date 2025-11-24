arr = [1,2,3,4,5]
print(arr)
arr[0] = arr[0] - 1
print(arr)
arr[-1] = arr[-1]+4
print(arr)
arr[len(arr)//2] = arr[len(arr)//2]*2
print(arr)


n = 0 
while n < len(arr):
    arr[n] = 0
    n = n + 1 
    print(arr)

arr[1:3] #weź wartości od wartości z numerem 1 do n-1 (3 otwarte tak jakby)
print(arr[1:3])