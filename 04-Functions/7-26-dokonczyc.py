def f(text):
    result=''
    for i in text:
        if i in text == len(text):
                result+=i
        else:
            result+=i+"-"
        
    return result

print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))
