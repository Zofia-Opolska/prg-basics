def f(n):
    i=1
    string=str()
    for i in range(1,n+1):
        if i<=n:
            string+=str(i)
            i+=1
    return string
print(f(11))
print(f(4))