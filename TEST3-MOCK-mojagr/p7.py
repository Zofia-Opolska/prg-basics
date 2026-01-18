class C:
    def __init__(self,c):
        self.c = c

    def m1(self):
        return self.c
    
    def m2(self):
        self.c += 1
    
    def m3(self):
        self.c -= 1

    def m4(self,n):
        self.c += n

    def __str__(self):
        self.c = str(self.c)
        return self.c
    
# c=C(5)
# print(c.m1())
# c.m2()
# print(c.m1())
# c.m4(-8)
# print(c.m1())
# c.m3()
# print(c.m1())
# c.m4(25)
# print(c.m1())
# c.__str__()
# print(type(c.m1()))