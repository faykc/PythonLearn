class Car:
    def __init__(self, company='None', year=0):
        self.company = company
        self.year = year
    def __str__(self):
        return '{} {}'.format(self.company, self.year)
    def isCar(self):
        return True

class BMW(Car):
    def __init__(self, year, wifi=True):
        super().__init__('BMW',year)
        self.wifi = wifi
    def __str__(self):
        return super().__str__() + ' {}'.format(self.wifi)

lol = BMW('2000', False)
print(lol)
print(lol.isCar())