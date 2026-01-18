class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        else:
            return 1
    def m2(self,a,b):
        self.a = a
        self.b = b

        cw=-1
        cw2=-1

        if self.x > 0 and self.y > 0:
            cw = 1
        elif self.x < 0 and self.y > 0:
            cw = 4
        elif self.x < 0 and self.y < 0:
            cw = 3
        elif self.x > 0 and self.y < 0:
            cw = 2

        if self.a > 0 and self.b > 0:
            cw2 = 1
        elif self.a < 0 and self.b > 0:
            cw2 = 4
        elif self.a < 0 and self.b < 0:
            cw2 = 3
        elif self.a > 0 and self.b < 0:
            cw2 = 2
        
        if cw == cw2:
            return True
        else:
            return False
        
    def m3(self,a,b):
        self.a = a
        self.b = b
        import math
        distance = math.sqrt((self.a - self.x) ** 2 + (self.b - self.y) ** 2)
        if distance > 5:
            return True
        else:
            return False

# p = C(2, 3)
# print(p.m1())        # 1
# print(p.m2(7, 4))    # True
# print(p.m2(-3, 1))   # False
# print(p.m3(8, 5))    # True
# print(p.m3(4, 7))    # False

# p1 = C(0, 5)
# print(p1.m1())       # 0
# print(p1.m2(4, 7))   # False
# print(p1.m2(-7, 0))  # True