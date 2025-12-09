arr=[15, 8, 31, 47, 2, 19]
new_arr=[]
# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

# zrobic loop i pusty arr i do tego nowego pustego dodawac wartosci od konca
n=len(arr)

while not len(arr)==len(new_arr):
    new_arr.append(arr[n-1])
    n-=1
print(new_arr)