# # (p8.py) Reverse Polish Notation (RPN) is a mathematical notation in which operators follow their operands, e.g. 2 3 + 
# # 4 *. Define a function f(expression) that, for an RPN expression, returns the value of that expression. The expression 
# # contains only non-negative integers and the + and - operators. Example: 
# # f("2 3 +")  5 
# # f("2 6 + 4 5 - +")  7 
# # f("11 7 + 15 - 14 +")  17 

# If the entered value is a number, push the number on to the stack
# If the entered value is an operator, pop two items from the top of the stack, do the calculation, and push the result of the operation on to the stack.
# If the entered value is an equal sign, pop the final result from the stack and display the result of calculation.

def f(expression):
    phrase = expression.split()
    RPN=[]
    for i in phrase:
        if i.isdigit():
            RPN.append(int(i))
        elif i == '+':
            b = RPN.pop()
            a = RPN.pop()
            RPN.append(a + b)
        elif i == '-':
            b = RPN.pop()
            a = RPN.pop()
            RPN.append(a - b) 
    return RPN[0]
print(f("2 6 + 4 5 - +"))
print(f("11 7 + 15 - 14 +"))