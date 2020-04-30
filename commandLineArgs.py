import sys

lst = sys.argv

# Determining product of command line arguments

product = 1

for x in lst:
    if (len(lst) <= 1):
        break
    elif(x == 'commandLineArgs.py'):
        continue
    product *= int(x)

print(product)


