s = {10,20,"string",10,10,10}
print(type(s))
s.update([99])
print(s)
s.remove(10)
print(s)

f=frozenset({10,20,30})
x=frozenset([10,23,30])
print(f)
print(x)
