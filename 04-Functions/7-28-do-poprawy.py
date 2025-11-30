def f(dice):
    count=0
    for i in dice:
        if (len(str(dice))-len(str(set(dice))))>count:
            count = i
print(f("5233165554211"))