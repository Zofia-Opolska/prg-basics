class C:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        if self.age<18:
            result=''
            result += self.first_name[0].lower()
            result += self.last_name[0].lower()
            result += str(self.age)

        elif self.age>=18:
            result=''
            result += self.first_name[0].upper()
            result += self.last_name[0].upper()
            result += str(self.age)
        return result
    

print(C("John","May",18))
print(C("John","May",16))