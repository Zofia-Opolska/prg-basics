###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    i=0
    for line in file:
        i+=1
        print(i, line, end="")

#plik początkowo nie działa bo folder txt jest w złym folderze
#mozna w terminalu wykonac komende cd 
#lub zamknac cały folder z repo file - close folder i potem otwieramy sam folder 