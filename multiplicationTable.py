x = int(input("Please give a number: "))
beg,end = [int(x) for x in input("Please give the beginning and ending: ").split(" ")]

for y in range(beg, end + 1):
    print(x,'*',y,'=',x*y)
