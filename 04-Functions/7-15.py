def f(detector):
    count=0
    for i in detector:
        if i=='+':
            count+=1
        elif count==3:
                return True
        else:
            count-=1
    else:
        return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))