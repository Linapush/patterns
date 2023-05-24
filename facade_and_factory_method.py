from datetime import datetime
from time import sleep

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f'{self.__class__.__name__}, {self.name}'

class Event:
    city: str
    _start: datetime
    _end: datetime
    responsible: Human

    def __init__(self): 
        pass

    def start(self, city, responsible, start: datetime=None, end: datetime=None) -> None:
        self.city = city
        self._start = start
        self._end = end
        self.responsible = responsible

    def start(self) -> None:
        if self._start:
            if self._start and self._start < datetime.now():
                print('Event уже начался')
                return
            answer = input('Вы хотите начать Event раньше? Введите "Yes" or "No"')
            if answer != "Yes":
                return
        self._start = datetime.now()

    def end(self) -> None:
        if self._end:
            if self._end < datetime.now():
                print('Event уже закончился.')
            answer = input('Вы хотите закончить Event досрочно? Введите "Yes" or "No"')
            if answer != "Yes":
                return
        self._end = datetime.now()

    def is_live(self) -> bool:  
        relevant_start = self._start and self._start < datetime.now()
        relevant_end = not self._end or self._end > datetime.now()
        return relevant_start and relevant_end
            

    def get_duration(self) -> None:
        if not self.is_live() and self._start and self._end < datetime.now():
            return self._end - self._start

    def is_finished(self) -> None:
        return not self.is_live() and self._start and self._end and self._end < datetime.now()


class Adapter:
    @staticmethod
    def get_duration_hours(event: Event):
        delta = event.get_duration()
        if not delta:
            return None
        return delta.total_seconds() / 36000


class PRDepartment:
    city: str
    rate: float
    def __init__(self, city, rate):
        self.city = city
        self.rate = rate

    def pay(self, event: Event):
        if self.city == event.city and event.is_finished():
            duration = Adapter.get_duration_hours(event)
            if not duration:
                print("Невозможно заплатитьб ивент еще не завершился")
                return
            payment = round(self.rate * duration), 2
            print(f'Нужно заплатить {payment} рублей {event.responsible}')

holidays = Event('Сочи', Human('Аристарх'))
department = PRDepartment('Сочи', 70)
holidays.start()
sleep(10)
holidays.end()
department.pay(holidays)