def f(palindrome):
    palindrome=list(palindrome)
    if list(palindrome)==list(reversed(palindrome)):
        return True
    else:
        return False
print(f("radar"))
print(f("12-11-21"))
print(f("book"))
