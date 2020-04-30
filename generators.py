def genRange(x,y):
    while (x<y):
        yield x
        x+=1

lol = list(genRange(1,10))
print(lol)
