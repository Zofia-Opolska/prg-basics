import queue

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
# cards.put('King of Hearts \u2665')    
# cards.put('Queen of Diamonds \u2666')  
# cards.put('Jack of Spades \u2660')     
cards.put(2)
cards.put(3)
cards.put(7)
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)
cards.put(10)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# # removes and prints elements from the top of the stack
# while not cards.empty():
#     card = cards.get()
#     print(card)
    
last = cards.get()
second_last = cards.get()
sum_last_two = last + second_last
print("Sum of last two numbers:", sum_last_two)


total=0
while not cards.empty():
    total += cards.get()
    
print(total)