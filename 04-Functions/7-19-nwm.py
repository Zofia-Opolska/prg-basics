def f(number):

    sum=0
    count={}
    for i in str(number):
        if i in count:
            count+=i
        if count>0:
            sum+=i
    return sum

print(f(1027))
print(f(230335))
print(f(513553007))

