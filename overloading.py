class C:
    def __init__(self,c):
        self.c = c
    def __lt__(self, other):
        if(self.c<other.c):
            return "obj1 is less than obj2"
        else:
            return "obj2 is less than obj1"
    def __eq__(self,other):
        if(self.c ==other.c):
            return "both are equal"
        else:
            return "both are unequal"
        
obj1 = C(8)
obj2 = C(3)
print("passed values:", obj1.c, obj2.c)
print(obj1 < obj2)

obj3 = C(4)
obj4 = C(5)
print("passed values:", obj3.c, obj4.c)
print(obj3 == obj4)