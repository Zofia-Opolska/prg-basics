def f(d):
    count=0
    sum=0
    for i in d.values():
        sum+=i
    avr=sum/len(d)
    for i in d.values():
        if i>avr:
            count+=1
    return count


# print(f({"LO231":150,"BA787":120,"NZ15":30})) # returns 2
# print(f({"LO231":150,"BA787":20,"NZ15":30})) # returns 1 