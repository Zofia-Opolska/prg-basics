def f(name):
    words = name.split()
    acronym = ''.join(word[0] for word in words)
    return acronym

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))