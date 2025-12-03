def month(n):
    n = int(input('Enter month number: '))
    if n == 1:
        return "Styczeń"
    elif n == 2:
        return "Luty"
    elif n == 3:
        return "Marzec"
    elif n == 4:
        return "Kwiecień"
    elif n == 5:
        return "Maj"
    elif n == 6:
        return "Czerwiec"
    elif n == 7:
        return "Lipiec"
    elif n == 8:
        return "Sierpień"
    elif n == 9:
        return "Wrzesień"
    elif n == 10:
        return "Październik"
    elif n == 11:
        return "Listopad"
    elif n == 12:
        return "Grudzień"
     
    else:
        print("Incorrect number innput")
print(f"The name of the month {n} is {month(n)}")