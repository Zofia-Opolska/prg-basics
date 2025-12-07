# (p8.py) Reverse Polish Notation (RPN) is a mathematical notation in which operators follow their operands, e.g. 2 3 + 
# 4 *. Define a function f(expression) that, for an RPN expression, returns the value of that expression. The expression 
# contains only non-negative integers and the + and - operators. Example: 
# f("2 3 +")  5 
# f("2 6 + 4 5 - +")  7 
# f("11 7 + 15 - 14 +")  17 


def f(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  
            stack.append(int(token))
        elif token == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
    
    return stack[0]


print(f("2 3 +"))
print(f("2 6 + 4 5 - +"))
print(f("11 7 + 15 - 14 +"))