def f(n):
    wynik='"'
    if n==1:
        return '"*"'
    while n>1:
        wynik+="*"+"/"
        n-=1
    if n==1:
        wynik+="*"
    return wynik + '"'
print(f(4))
print(f(0))
print(f(1))
print(f(7))
