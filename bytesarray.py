lst=[1,2,3,4,5]
s={1,2,3,4,5}
b=bytes(lst)
c=bytes(s)
print(type(b), type(c))
print(b)

d = bytearray(lst)
print(d)
d[0]=10
print(d)
