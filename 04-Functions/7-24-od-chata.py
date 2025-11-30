def f(expression):
    total = int(expression[0])      # start with the first number
    i = 1

    while i < len(expression):
        op = expression[i]         # '+' or '-'
        num = int(expression[i+1]) # next digit

        if op == '+':
            total += num
        else:  # op == '-'
            total -= num

        i += 2

    return total


print(f('2+3'))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
