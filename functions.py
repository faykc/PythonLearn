
def average(nums : list):
    sum = 0
    for x in nums:
        sum += x
    return sum/len(nums)

print(average([1,2,3,4,5,6]))

def multipleReturn(*x):
    return x[0],x[1]

print(multipleReturn(1,2))

def stuff(x,y):
    print(x,y)

z = stuff
z(1,2)

def isOdd(x):
    print("Even") if (x % 2 == 0) else print("Odd")

def numComprehension(lst, func):
    for x in lst:
        func(x)

numComprehension(range(10), isOdd)

