class type1:
    def deftype1(self):
       print("get the 1") 
    def deftype2(self):
       print("get the 2") 
    def deftype3(self):
       print("get the 3")       
class type2:
    def deftype1(self):
       print("get the 1") 
    def deftype2(self):
       print("get the 2") 
    def deftype3(self):
       print("get the 3")    


obj1 = type1()
obj2 = type2()
for i in (obj1,obj2):
  i.deftype1()
  i.deftype2()
  i.deftype3()


 
