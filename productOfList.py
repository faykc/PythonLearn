lst = [int(x) for x in input("Please give me a list of numbers: ").split(" ")]

product = 1

for x in lst:
    product *= x

print(product)
