arr = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15]
       ]
arr_hold=[]

for rows in arr:
    for i in rows:
        print(i,end=" ")
    print()

arr_hold=arr[0][0]
arr[0][0]=arr[0][4]
arr[0][4]=arr_hold

arr_hold=arr[1][0]
arr[1][0]=arr[1][4]
arr[1][4]=arr_hold

arr_hold=arr[2][0]
arr[2][0]=arr[2][4]
arr[2][4]=arr_hold

print()
print('After changes:')
print()

for rows in arr:
    for i in rows:
        print(i,end=" ")
    print()