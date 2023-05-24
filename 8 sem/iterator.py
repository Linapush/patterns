# Итераторы полезны, когда есть небольшие последовательности

from random import choice
from string import ascii_letters

class RandomLetter:
    def __init__(self, letters_num: int):
        self.num = letters_num
        self.current = 0
        self.used = [] #already use letters

    def __next__(self):
        if self.current < self.num:
            letter = choice(ascii_letters)
            while letter in self.used:
                letter = choice(ascii_letters)
            self.current += 1
            return letter
        else:
            raise StopIteration #если вызывать его циклом, будет работать нормально

    def __iter__(self):
        return self

# letter_iterator = RandomLetter(2)
# for letter in letter_iterator:
#     print(letter)

class Iterator:
    def __init__(self):
        self.instances = []

    def add(self, instance: any):
        self._instances.append()

    def remove(self, instance: any):
        try:    
            self._instances.remove(instance)
        except Exception as error:
            print(f'error while instance of {instance.__class__.__name__} iterator: {error}')

    def __next__(self):
        if self._instances:
            return self._instances.pop()
        else:
            raise StopIteration

    def __iter__(self):
        return self

class Person:
    iterator = Iterator()

    def __init__(self, name: str, age: int):
        self.name, self.age = name, age
        Person.instances.append(self)   #экземпляры

    def __del__(self):
            Person.iterator.remove(self)

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name}, {self.age} y. o.'
        
petya = Person('Petya', 20)
vasya = Person('Vasya', 19)
vladislav = Person('Vlad', 18)
for person in Person.iterator:
    print(person)

# print(next(letter_iterator))
# print(next(letter_iterator))
# print(next(letter_iterator))

# в фреймворках(в моделях) есть цикл, (filter, )