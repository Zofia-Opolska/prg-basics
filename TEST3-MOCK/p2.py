def f(tekst):
    count=0
    for i in tekst:
        if i == "+":
            count+=1
        elif i == "-":
            count-=1
    return count

print(f("+--+"))
print(f("+-+++++++-+"))
print(f(""))