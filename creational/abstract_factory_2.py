

class Vehicle:
    def __init__(self, domain=None):
        self.domain = domain

    def type_vehicle(self) -> str:
        return self.__class__.__name__
    
    def get_domain(self) -> str:
        return self.domain if self.domain else 'not assigned'
    
    def __str__(self):
        return f'{self.type_vehicle()}, Domain: {self.get_domain()}'


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


if __name__ == '__main__':
    # using type
    motorcycle = type('Motorcycle', (Vehicle,), dict())('123AA')
    car_1 = type('Car', (Vehicle,), dict())('AA123AA')
    car_2 = type('Car', (Vehicle,), dict())()
    
    print(motorcycle) # Motorcycle, Domain: 123AA
    print(car_1) # Car, Domain: AA123AA
    print(car_2) # Car, Domain: not assigned
    
    # using class
    motorcycle = Motorcycle('123AA')
    car_1 = Car('AA123AA')
    car_2 = Car()

    print(motorcycle) # Motorcycle, Domain: 123AA
    print(car_1) # Car, Domain: AA123AA
    print(car_2) # Car, Domain: not assigned
    


    