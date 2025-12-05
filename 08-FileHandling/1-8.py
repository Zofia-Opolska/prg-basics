with open("pets.txt") as file:
    content = file.read()
    list_of_words= content.split()
    print(len(list_of_words))