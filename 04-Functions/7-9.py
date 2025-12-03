def f(number,even):
    sum_even=0
    sum_odd=0
    for i in str(number):
        if i in ['0','2','4','6','8']:
            sum_even+=int(i)
        elif i not in ['0','2','4','6','8']:
            sum_odd+=int(i)
    if even == True:
        return sum_even
    elif even == False:
        return sum_odd
    
print(f(3124,True))
print(f(3124,False))
print(f(13115,True))
print(f(0,True))
print(f(0,False))