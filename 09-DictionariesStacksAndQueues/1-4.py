person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])
print(person)
person["surname"]="Nowak"
print(person["surname"])
person["married"]=False
print(person["married"])
person["gnder"]="male"
person["hobby"].append("bicycle")
print(person["hobby"])
person["phone"]["work"]='313131444'
print(person["phone"])

# Then, create a program that:
# Displays name
# Displays hobby
# Displays the entire contents of the dictionary
# Changes surname to 'Nowak'
# Changes person's marriage status
# Adds gender: 'male'
# Adds a new hobby: 'bicycle'
# Adds work phone to existing phones: '313131444'
# Displays the entire contents of the dictionary (iterate over dictionary items)