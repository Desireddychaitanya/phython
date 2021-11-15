class base:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

class child(base):
    def __init__(self, name,age):
        self.name = name
      
        base.__init__(self,name,age)
    def getname1(self):
        return self.age    

class grandchild(child):                              
    def __init__(self, name, age):
        child.__init__(self,name,age)

    def getname2(self):
        return self.age    


obj = grandchild("vishnu",23)
print(obj.getname())
print(obj.age)




        