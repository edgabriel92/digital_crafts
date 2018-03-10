class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        return '{} \n{} \n{}'.format(self.make, self.model, self.year)
         


car1 = Vehicle('Nissan', 'Versa', 2015)
car2 = Vehicle('Honda', 'Civic', 2016)
car3 = Vehicle('Toyota', 'Corolla', 2011)

print Vehicle.print_info(car1) # 2 ways to print information
#print car1.print_info()