#clasa która po podaniu imienia i wieku wypluwa pierwsza literę imienia i wiek duża litera jeśli osoba ma >18 lat
class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        if self.age>=18:
            result = ""
            result += self.name[0].upper()
            result += "-"
            result += str(self.age)
            return result
        else:
            result = ""
            result += self.name[0].lower()
            result += "-"
            result += str(self.age)
            return result

print(C('John',18))
print(C('Maya',8))
print(C('Abigail',28))