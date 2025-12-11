def f(n):
    import queue
    stack = queue.LifoQueue()
    while n/2 != 0:
        r=n%2
        stack.put(r)
        n=n//2

    binary = ""
    while not stack.empty():
        binary += str(stack.get())
    return binary
        
print(f(18))
