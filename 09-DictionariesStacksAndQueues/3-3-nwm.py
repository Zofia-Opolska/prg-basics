import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   stack=queue.LifoQueue()
   for i in expression:
      if i in ['[','{','(']:
         stack.put(i)
      elif i in [']','}',')']:
         if stack.empty():
            return False
 
 
print(brackets_ok("[(2+3)*4+5]/6-{(7*8)+[4]}"))
print(brackets_ok("[(2+3]/4)"  ))
print(brackets_ok("(2-3*4+(5/6)" ))

############################

import queue

def brackets_ok(expression):
    stack = queue.LifoQueue()
    for ch in expression:
        if ch in ['[', '{', '(']:
            stack.put(ch)
        elif ch in [']', '}', ')']:
            if stack.empty():   # no matching opening bracket
                return False
            last = stack.get()
            # check matching pair
            if ch == ']' and last != '[':
                return False
            if ch == '}' and last != '{':
                return False
            if ch == ')' and last != '(':
                return False

    return stack.empty()
