def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

def sub(n):
    return n+n

numbers = (1,23,34,56)
r = map(sub, numbers)
print(list(result))