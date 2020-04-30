from functools import reduce

nth = lambda x,n: x**n

print(nth(5,3))

yesNo = lambda x: 'YES' if (x%2==0) else 'NO'

print(yesNo(3))

l = list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7]))

for x in l:
    print(x)

print(l)

double = list(map(lambda x: 2*x, range(10)))
print(double)

sumList = reduce(lambda x,y: x+y, [1,2,3])
print(sumList)

def foldr(x,lst : list):
    result = 0
    for y in lst:
        result = x(y,result)
    return result

print(foldr(lambda x,y: x+y, [1,2,3]))