# существуют машины с общими свойствами и методы
# свойтсва: кол-во колес, двигатель, кол-во мест
# методы: установить кол-во колес, установить двигатель, установить кол-во мест
# есть конкретные машины с кокретнами свойствами
# свойства и методы те же только со значениями
from abc import ABC, abstractmethod

class Engine:
    def __init__(self, manf: str, hp: int):
        self.manf, self.hp

class Car(ABC):   
    wheels: int = 4
    seats: int
    engine: Engine

    @abstractmethod
    def set_seats(self) -> None:
        pass

    def set_engine(self, hp) -> None:
        self.engine = Engine(self.__class__.__name__, hp)

    def __str__(self):
        carname = self.__class__.__name__
        return f'{carname} with {self.wheels} wheels, {self.seats} seats'

class LadaCar(Car):
    def set_seats(self) -> None:
        self.seats = 5
    
class MaybachCar(Car):
    def set_seats(self) -> None:
        self.seats = 4

# принимает класс какого-то объекта, принимая методы
class CarBuilder(Car):
    def build(self, car_class, hp):
        car = car_class()
        car.car_seats()
        car.set_engine(hp)
        return car

cb = CarBuilder()
print(cb.build(LadaCar, 85))
print(cb.build(MaybachCar, 300))


    # def set_car(self, car : int) -> None:
    #     self.__car = car
 
    # def setup_car(self, hp: int) -> None:
    #     self.__car.set_engine(hp)
    #     self.__car.set_seats()

    # def get_car(self):
    #     return self.__car
