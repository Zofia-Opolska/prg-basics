def f(card_number):
    arr=[1,2,'*','*','*','*','*','*','*','*','*','*',3,4,5,6]
    arr[0]=int(card_number[0])
    arr[1]=int(card_number[1])
    arr[12]=int(card_number[12])
    arr[13]=int(card_number[13])
    arr[14]=int(card_number[14])
    arr[15]=int(card_number[15])

    ciąg=""
    for i in arr:
        if i in [0,1,2,3,4,5,6,7,8,9,'*']:
            ciąg+=str(i)
    return ciąg
   


print(f("5290312400019022"))

