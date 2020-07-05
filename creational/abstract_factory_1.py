

class Vehicle():

    def __init__(self, vehicle_factory):
        self.vehicle_factory = vehicle_factory
    
    def type_vehicle(self) -> str:
        return self.vehicle_factory.__name__
    
    def domain(self) -> str:
        return self.vehicle_factory.domain if hasattr(self.vehicle_factory, 'domain') else 'not assigned'
    
    def __str__(self):
        return f'{self.type_vehicle()}, Domain: {self.domain()}'


if __name__ == '__main__':
    motorcycle = Vehicle(type('Motorcycle', (), dict(domain='123AA')))
    car_1 = Vehicle(type('Car', (), dict(domain='AA123AA')))
    car_2 = Vehicle(type('Car', (), dict()))
    
    print(motorcycle) # Motorcycle, Domain: 123AA
    print(car_1) # Car, Domain: AA123AA
    print(car_2) # Car, Domain: not assigned
    


    