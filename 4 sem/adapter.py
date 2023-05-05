# Паттерн Адаптер
# HDMI, ноут
# Розетка, тарансформатор
# Уже вижу задания по паттернам

# Нам важно, что у нас есть внешний интерфейс трансформатора, 
# мы используем адаптер, когда внешний интерфейс нас не устраивает

from abc import ABC
from random import uniform #берет от float до float

class Transformer:
    voltage: int
    fluct_range: float

    # можем сделать метод абстрактным, так метод будет у любого класса
    def get_current_voltage(self):
        return round(self.voltage + uniform(-self.fluct_range, self.fluct_range), 2) 

class Transformer220(Transformer):
    voltage = 220
    fluct_range = 20

class Transformer380(Transformer):
    voltage = 380
    fluct_range = 30

# Трансформаторы
transformer_1 = Transformer220()
print(transformer_1.get_current_voltage())
transformer_2 = Transformer380()
print(transformer_2.get_current_voltage())


# Смысл - создать розетку
# Адаптируем класс трансформер под розетку

class PowerSocket:
    def __init__(self, transformer: Transformer, slots_num: int):
        self.transformer = transformer
        self.slots_num = slots_num

    def voltage(self):
        print(f'{self._class__.__name__}, voltage = {self.transformer.voltage}')

    def current_voltage(self):
        print(f'{self.__class__.__name__}, current_voltage = {self.transformer.get_current_voltage()}')

ps_220 = PowerSocket(Transformer220(), 3)
ps_220.voltage()
ps_220.current_voltage
