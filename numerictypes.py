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
print(type(z)) # Yields (float), converted automatically, (could be dangerous)..

d = 2 + 5j  # This would not be allowed in C HOLY!
print(d)
print(type(d))  # Strange complex types

e = 0B1010  # Binary Value
print(e)
print(type(e)) # Prints <int>

f = 0XFF    # Hexadecimal
print(f)

o = 0o74 #Octodecimal value
print(o)

g = True # Decimal values
h : bool = False
print(g)
print(h)
print(type(g))
print(type(h))

print(10 < 15)
print(type(10 < 15))

h = int(45.6) # Casting it to an integer?
print(h)
print(type(h))

i = float("22.5")
print(i)
print(type(i))

x = bin(10)
print(x)
print(type(x))
