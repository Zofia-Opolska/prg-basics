# (p1.py) The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 
# each. The other cards have the value indicated by the card number. Define a function f(player1,player2) that returns 
# true if the first player has cards of the same or higher value, and false otherwise. Example: 
# f("AJ972","AQT72")  False 
# f("9532","K8")  True 

#1st player cards of the same value or higher

def f(player1,player2):
    cards={
        'A':10,
        'K':10,
        'Q':10,
        'J':10,
        'T':10,
        '9':9,
        '8':8,
        '7':7,
        '6':6,
        '5':5,
        '4':4,
        '3':3,
        '2':2,
        '1':1,
    }
    val_1=0
    val_2=0
    for i in player1:
        if i in cards:
            val_1+=cards[i]
    for i in player2:
        if i in cards:
            val_2+=cards[i]
    if val_1>=val_2:
        return True
    else:
        return False
print(f("AJ972","AQT72"))
print(f("9532","K8"))
    
