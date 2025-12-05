open("example.txt","r") #r oznacza że otwieramy plik do odczytu, mozemy pisac bez tego tak jak ponizej
open("example.txt")
open("example.txt","w") #otwieramy plik i mozemy cos do niego wpisac, automatycznie czyści plik jezeli cos na nim wczesniej bylo
open("example.txt", "a") # nie usuwa danych które były w pliku , pozwala dodac nowe dane na koniec pliku


file = open("example.txt","r") #funkcja open zwraca wskaźnik do pliku (identyfikator)
...#operacje na pliku
file.close #funkcja zamykająca plik

#############################

file = open("example.txt","r") 
content = file.read()
file.close 

print(content)

#############################

with open('example.txt', 'r') as file:
   content = file.read()
# The file is automatically closed when the block is exited

print(content)

#############################
