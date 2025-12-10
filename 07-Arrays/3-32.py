arr = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15]
       ]
arr_hold=[]
arr_hold=arr[0]
arr[0]=arr[2]
arr[2]=arr_hold
print(arr)

##
print(list(reversed(arr)))