lst = [x**3 for x in range(10)]
print(lst)

evenLst = list(filter(lambda x: x%2==0, [x for x in range(21)]))
print(evenLst)

evenLst2 = [x for x in range(0,21,2)]
print(evenLst2)

evenLst3 = [x for x in range(21) if x%2==0]
print(evenLst3)


# Assumption: len(lst1) = len(lst2)
def productLst(lst1 : list, lst2 : list):
    productlst = []
    for x in range(len(lst1)):
        productlst.append(lst1[x] * lst2[x])
    return productlst

print(productLst([1,2,3],[1,2,3]))

a = [1,2,3]
b = a
productlst = [a[i] * b[i] for i in range(len(a))]

