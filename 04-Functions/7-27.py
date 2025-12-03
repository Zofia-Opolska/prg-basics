def f(code):
    code=list(str(code))
    sum=int(code[0])+int(code[1])+int(code[2])
    d = sum%7
    if int(code[3])==d:
        return True
    else:
        return False
    
 
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))

