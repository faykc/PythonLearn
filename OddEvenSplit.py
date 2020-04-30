beg, end = [int(x) for x in input("Please enter the beginning and ending numbers: ").split(" ")]
evens = []
odds = []

while (beg <= end):
    evens.append(beg) if (beg % 2 == 0) else odds.append(beg)
    beg += 1

print('The odd numbers are as follows {}'.format(odds))

