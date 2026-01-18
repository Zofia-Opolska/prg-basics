class C:
    def __init__(self,stadion):
        self.stadion = stadion

    def m1(self,s,n):
        self.s = s
        self.n = n #czy mozna to usunac?
        self.stadion[s] = n
    def m2(self,s):
        self.s = s
        sum = 0
        for i in s:
            if i in self.stadion:
                sum += self.stadion[i]
        return sum
    
stadium = C({"A":120,"D":150,"G":90,"K":110})
stadium.m1("G",130)
print(stadium.m2("GD"))
print(stadium.m2("KEJ"))

