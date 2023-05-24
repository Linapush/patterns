# Observer - тот, кто следит за событием/изменениями и тд
# Observable - тотб кто производит изменения и устанавливает событие
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Observarable(ABC):
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscribe: Observer):
        self.subscribers.append(subscribe)

    def notify_all(self, message: str):
        for sub in self.subscribers:
            self.update(message)

class CollegeSiriusVKPage(Observarable):
    def publish(self, post: str):
        self.notify_all(f'{self.__class__.__name__}: {post}')

class Student(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f'{self.__class__.__name__} {self.name} get message {message}')

sirius_vk_page = CollegeSiriusVKPage()
sirius_vk_page.subscribe(Student('Vasya'))
sirius_vk_page.subscribe(Student('Petya'))
sirius_vk_page.publish('1.11.1 programming lessons are remote today')