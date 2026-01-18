class C:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        if self.age<18:
            name=''
            name+=self.first_name[0].lower()
            name+=self.last_name[0].lower()
            name+=str(self.age)
            return name
        
        elif self.age>=18:
            name=''
            name += self.first_name[0].upper()
            name += self.last_name[0].upper()
            name += str(self.age)
            return name
    


# print(C("John","May",21))
# print(C("Anna","Brown",17))