def f(amount_to_pay):
    count=0
    if amount_to_pay==0:
        return 0
    else:
        while amount_to_pay >=5:
            count+=1
            amount_to_pay-=5
        while amount_to_pay >=2:
            count+=1
            amount_to_pay-=2
        while amount_to_pay >=1:
            count+=1
            amount_to_pay-=1
        return count

print(f(23))
print(f(8))
print(f(2))
print(f(0))