n = (12,23,34,45,56)



result = map(lambda x : x + x,n )
print(list(result))




# Add two lists using map and lambda
  
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

num1 = [1,2,3]
num2 = [12,23,34]


result = map(lambda x,y:x+y,num1,num2)
print(list(result))
num1 = [10,12,23,34,343,111111,1111111,111111111,1]
num2 = [12,23,23,23,23]
num3 = [12]
result = map(lambda a,b,c:a+b+c,num1,num2,num3)
print(list(result))

l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)



