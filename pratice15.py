class base1:
    def __init__(self):
        self.name1 = "ashik"
        self.age = 23

    def age1(self):
        return self.age;   

class base2:
    def __init__(self):
        self.name2 = "yashil"
        self.agebase = 21
    def age2(self):
        return self.age;   

class derived(base1,base2):
    def __init__(self):
     base1.__init__(self)
     base2.__init__(self)    
     self.name ="chaitu"    
obj = derived()
print(obj.name)        
print(obj.name1)
print(obj.name2)

print(obj.age1())


        