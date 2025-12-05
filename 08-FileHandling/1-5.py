
with open('countries.txt', 'r') as file:
    counter=0
    for line in file:
        i+=1
        print(f"{counter}.{line}",end="")