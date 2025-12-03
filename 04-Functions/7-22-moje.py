def f(name):
    string=str(name)
    new_string=''
    for i in str(name):
        if i == string[0]:
            new_string+=i
        elif i == ' ':
            new_string+=string[i+1]
    return new_string
print(f("Internet of Things"))