def f(password):
    if len(password)>=6 and (len(password) == len(set(password))):
            return True
    else:
        return False
    
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
