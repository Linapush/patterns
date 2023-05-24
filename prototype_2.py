class Human:
    pass

class Prototype:
    def prototype(self):
        class_name = self.__class__.__name__
        bases = self.__class__.__bases__
        attrs = dict(self.__class__.__dict__)
        class_ = type(class_name, bases, attrs)
        initial_attrs = dict()
        for attr, value in self.__dict__.items():
            try:
                initial_attrs[attrs] = value.copy()
            except:
                initial_attrs[attr] = value
        return class_(**initial_attrs) #мы распаковываем словарь **

#проблема в том, что св-ва сылаются на список, список ссылается на объект 
#у Пети 2 родственник тоже станет Аня

class Person(Human, Prototype):
    def __init__(self, name: str) -> None:
        self.name = name

    def say(self, text: str):
        print(f'{self.name}: {text}') #простой оюъект для копирования

petya_1 = Person('Petya')
petya_2 = petya_1.prototype()
print(petya_1, petya_2)
print(petya_1.name, petya_2.name)