class Car:
    def __init__(self, company='None', year=0):
        self.company = company
        self.year = year
    def __str__(self):
        return '{} {}'.format(self.company, self.year)

class BMW(Car):
    def __init__(self, year, wifi=True):
        Car.__init__(self,'BMW',year)
        self.wifi = wifi
    def __str__(self):
        return Car.__str__(self) + ' {}'.format(self.wifi)

lol = BMW('2000', False)
print(lol)