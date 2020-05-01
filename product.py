class Product:
    def __init__(self,name='name',description='desc',price=0):
        self.name=name
        self.description=description
        self.price=price
    
    def __str__(self):
        return 'Name: {}, Description: {}, Price: {}'.format(self.name,self.description,self.price)

p1 = Product("Bob","Description",10)
print(p1)


    
    


