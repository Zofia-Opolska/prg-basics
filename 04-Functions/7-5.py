def f(n,x,y):
    if n in range(x,y+1):
        return True
    else:
        return False
    
print(f(5,3,5))
print(f(0,3,4))
print(f(5,3,6))
print(f(3,3,6))