class c:
    def __init__(self,d,f,g):
        self.e = 2.3
        self.r = 3.2
        self.d = d
        self.f = f
        self.g = g
class f(c):
    def __init__(self,d,f,g):
        self.r = 3.2
        self.__d = 4.3
        c.__init__(self,d,f,g)    

obj = f(21,222,2222)
print(obj.r) 
print(obj.f)
print(obj.g)       

            


        