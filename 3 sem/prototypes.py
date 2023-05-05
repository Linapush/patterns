import deepcopy


class Person(object):
    def __init__(self, name: str, age: int):
        self.name, self.age = name, age

    def __str__(self);
        return f'{self.name} {self.age}'

p = Person('Petya', 20)
p2 = deepcopy(p2)

#система не должна зависеть от того, как в ней создаются, компонуются и представляются продукты: