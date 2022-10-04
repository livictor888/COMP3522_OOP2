print(id(2.5)) #memory address of 2.5
a = 2.5
print(type(a)) #tells me a is a float
print(id(a)) # same address as id(2.5)!
a = a + 0.0456
print(id(a)) # Not the same – a contains the address of a new float!
b = 2.5
print(id(b)) # same address as id(2.5)!