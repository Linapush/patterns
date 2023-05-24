from datetime import datetime
from time import sleep

class Human:
    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name}'

class Event:
    city: str
    _start: datetime
    _end: datetime
    responsible: Human
    
    def __init__(self, city, responsible, start: datetime=None, end: datetime=None):
        self.city, self._start, self._end, self.responsible = city, start, end, responsible
    
    def start(self) -> None:
        if self._start:
            if self._start < datetime.now():
                print('Event уже начался.')
                return
            answer = input('Вы хотите начать ивент раньше? Введите "Yes" или "No')
            if answer != "Yes":
                return
        self._start = datetime.now()

    def end(self) -> None:
        if self._end:
            if self._end < datetime.now():
                print('Event уже закончился.')
                return
            answer = input('Вы хотите закончить ивент раньше? Введите "Yes" или "No')
            if answer != "Yes":
                return
        self._end = datetime.now()
    
    def is_live(self) -> bool:
        relevant_start = self._start and self._start < datetime.now()
        relevant_end = not self._end or self._end > datetime.now()
        return relevant_start and relevant_end
        
    
    def get_duration(self):
        if self.is_finished():
            return self._end - self._start
    
    def is_finished(self) -> bool:
        return not self.is_live() and self._start and self._end and self._end < datetime.now()

class Adapter:
    @staticmethod
    def get_duration_hours(event: Event):
        delta = event.get_duration()
        if not delta:
            return None
        return delta.total_seconds() / 3600

class Department:
    city: str
    rate: float
    
    def __init__(self, city, rate):
        self.city, self.rate = city, rate
    
    def pay(self, event: Event):
        if self.city == event.city and event.is_finished():
            duration = Adapter.get_duration_hours(event)
            if not duration:
                print("Невозможно заплатить, ивент еще не завершился.")
                return
            payment = round(self.rate * duration, 2)
            print(f'Нужно заплатить {payment} рублей {event.responsible}.')

holidays = Event('Сочи', Human('Петя'))
department = Department('Адлер', 70)
holidays.start()
sleep(9)
holidays.end()
department.pay(holidays)