def f(sentence):
    string=''
    for i in sentence:
        if i not in (" "):
            string+=i
    return string

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))
