tp = ()
print(tp) #Empty tuple

x=(39,) #Must include , otherwise will not be considered a tuple
print(x)

z=(1,2,3,4,[67,67,90,""],'last element')
print(z)
print(type(z))
print(z[4])
print(z[4][0])
print(z.count(2))
print(z.index(1))