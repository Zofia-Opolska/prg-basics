def f(x,y):
    count=0
    for x in (range(x,y+1)):
        if x<0 and x%2==0:
            count+=1
    return count

print(f(-8,-2))
print(f(-7,8))
print(f(-1,11))
