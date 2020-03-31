a = 10
b : int = 50   # Making Python Typesafe!!
print(a + b)
print(a,b)

x = 45.3
y : float = 37.8
z : float = 37
print(x+y)
print(x,y)
print(x,y,z) 
print(type(z))  # Yields (int) intersting, it converted it automatically

z = 37.1
print(type(z)) # Yields (float)

z = 30
z += 0.1
print(z)
print(type(z)) # Yields (float), converted automatically, could be dangerous...

