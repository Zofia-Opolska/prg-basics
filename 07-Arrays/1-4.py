###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0]) #liczymi od 0
print('Second value', arr[1])
print('Last value', arr[-1])#nie mozemy dac 4 bo ilosc elementow moze sie zmieniac
print(arr[len(arr)-1])
print(arr[len(arr)-2])
print('Sum of 1st and last valu is', arr[0]+arr[-1])
print('Middle value is', arr[2]) # czy jest na to jakis inny sposob?

#nwm ocs takiego?
for i in arr:
    print(i)

