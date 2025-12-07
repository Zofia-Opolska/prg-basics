# (p2.py) An array contains at least 3 integers. All numbers in the array are equal except one. Define a function f(arr) 
# that returns a number in the arr array that is different from the other numbers. Example: 
# f([7,7,7,7,7,5,7,7])  5 

def f(arr):
    number=0
    i=0
    if len(arr)>3:
        while arr[i] == arr[i+1]:
            i+=1
        else:
            number=arr[i+1]
        return number
print(f([7,7,7,7,7,5,7,7]))


#kod z gówna ulepiony tak szczerze 
# ale działa? działa