nums = [int(x) for x in input("Please enter K numbers seperated by single space: ").split(' ')]
sum = 0

for x in nums:
    sum += x

print('The Average is {}'.format(sum/len(nums)))

