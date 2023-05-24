# Компоновщик
# Пенал: в нем есть ручки и карандаши
# В списке 
# В компоновщике при удалении и добавлении мы можем создать свою логику
# TODO
# добавить удаление элементов по особой логике

# Компоновщик
from abc import ABC

class Stationery:
    lead: str
    ttl: float
    color: str

    def __init__(self, color: str, ttl: float):
        self.color, self.ttl = color, ttl

    def draw(self, dist: float):
        print(f'Drawing {dist} meters')
        new_ttl = self.ttl - dist / 100
        self.ttl = new_ttl if new_ttl >= 0 else 0

    def __str__(self):
        return f'{self.color} {self.__class__.__name__} with {self.ttl} time to leave left'

class Pen(Stationery):
    lead = 'ink'

class Pencil(Stationery):
    lead = 'carbon'

class Case:
    def __init__(self):
        self.__stationery = []

    def add(self, unit: Stationery):
        if isinstance(unit, Stationery):
            self.__stationery.append(unit)

    def remove(self, unit: Stationery):
        if isinstance(unit, Stationery):
            self.__stationery.remove(unit)
        else:
            print(f'{unit} was not found in case stationery')
    
    def get_available_meters(self):
        acc = 0
        for unit in self.__stationery:
            acc += unit.ttl * 100
        return acc

    def stationery(self):
        return self.__stationery

new_case = Case()
pencil = Pencil('red', 100)
pencil.draw(100)
print(pencil)
pen = Pen('blue', 100)
new_case.add(pen)
new_case.add(pencil)
print([str(unit) for unit in new_case.stationery()])
print(f'We can draw {new_case.get_available_meters()} with case stationery')
new_case.remove(pencil)
print([str(unit) for unit in new_case.stationery()])