# существуют заводы
# на заводах делают машины, на люббом заводе можно произвести машину (общее)
# на конкретных заводах делают конкретные машины и мотоциклы
# Vehicle --> Motocycle, Car
# у всех транспортных средств есть свойства цена (общее)
# у всех машин есть вместимость (кол-во мест)
# у мотоцикла есть passenger_seat
# у мотоциклов есть bool_pasenger_seat (частное относительно ТС, общее для мотоциклов)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    price : int
    factory: str

    def __init__(self, factory_name: str, price: int = 0):
        self.factory = factory_name
        self.price = price

    def __str__(self):
        return f'{self.__class__.__name__} made by {self.factory}, costs {self.price}'

    def set_price(self, new_price: int):
        if isinstance(new_price, int) and new_price >= 0:
            self.price = new_price
    
    def get_price(self):
        return self.__price
    
    price = property(get_price, set_price)

class Car(Vehicle):
    seats: int

class Motorcycle(Vehicle):
    passenger_seat: bool

class AbstractFactory(ABC):
    @abstractmethod
    def create(self) -> Vehicle:
        pass 

class AbstractMotorcycleFactory(AbstractFactory):
    def create(self) -> Car:
        return Motorcycle(self.__class__.__name__)
    
class AbstractCarFactory(AbstractFactory):
    def create(self) -> Car:
        return Motorcycle(self.__class__.__name__)
    
class ToyotaCarFactory(AbstractCarFactory):
    price = 100

    def create(self) -> Car:
        return Car(self.__class__.__name__, self.price)

class YamahaMotorcycleFactory()

yamaha_moto_factory = YamahaMotorcycleFactory()
yamaha_motorcycle = yamaha_moto_factory.create()
print(yamaha_moto_factory)
