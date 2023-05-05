# Паттерн Фасад
# Фасад - паттерн, структурирующий объект
# Нас не интересует внутренний процесс, нам важно нажать кнопка 
# Одним методом или оним интерфейсом запускается 1 компьютер, не нужно запускать дополнительно ничего
# Здесь мы не используем составные части подсистемы

from abc import ABC

class Board(ABC):
    active = False

    def turn_on(self):
        self.active = True

    def turn_of(self):
        self.active = False

class MotherBoard(Board):
    power_supply: float

    def __init__(self, power_supply: float):
        self.power_supply = power_supply

class Display(Board):
    diagonal: float

    def __init__(self, diagonal: float):
        self.diagonal = diagonal

class Computer:
    def __init__(self, motherboard: MotherBoard, display: Display):
         self.motherboard, self.display = motherboard, display

    def run():
        pass

computer = Computer(MotherBoard(5.0), Display(15.6))
computer.run()
print(computer.motherboard.active())