A0 = dict(zip(('a','b','c','d','e'),(1,23,3,4,5)))
print(A0)

for i in range(0,10):
 for j in range(0,i+1):
     print(j,end=' ')
 print('\n')

A3 = sorted([A0[s] for s in A0])
A=[]
for s in A0:
    print(s)
    print(A0[s])
    A.append(A0[s])
print(A)    
A.sort()
print(A)    
