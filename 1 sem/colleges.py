# существуют колледжи
# в колледжах можно учиться определенным (абстрактные) технологиям (общее)
# в конкретных колледжах используются конкретные технологии (частное)
# в колледжах можно пойти на практику (УП, ПП) (общее)
# в конкретных колледжах можно пойти на практику в конкретные места (частное)
from abc import ABC, abstractmethod
from random import choice

class Technology(ABC):
    pass

class WorkPractice(ABC):
    @abstractmethod
    def get_practice(self, techology: Technology):
        work_name = self.__class__.__name__
        tech_name = techology.__class__.__name__
        print(f'We went to {work_name} to practice {tech_name}')

class College(ABC):
    @abstractmethod
    def get_technology(self) -> Technology:
        pass

    @abstractmethod
    def get_work_practice(self) -> WorkPractice:
        pass

class PythonDjango(Technology):
    pass

class ReactJS(Technology):
    pass

class Pascal(Technology):
    pass


class VkPractice(WorkPractice):
    def get_practice(self, techology: Technology):
        super().get_practice(techology)
        print('And got a lot of knowledge')

class GreenAtom(WorkPractice):
    def get_practice(self, techology: Technology):
        super().get_practice(techology)
        print('and we got a lot of useful work')

class HoofAndHornsPractice(WorkPractice):
    def get_practice(self, techology: Technology):
        super().get_practice(techology)
        print('And did nothing there')


class UsualCollege(College):
    def get_technology(self):
        return Pascal()
    
    def get_work_practice(self) -> WorkPractice:
        return HoofAndHornsPractice()
    

class SiriusCollege(College):
    def get_technology(self):
        return choice([PythonDjango, ReactJS])()
    
    def get_work_practice(self) -> WorkPractice:
        return choice([VkPractice, GreenAtom])()
    

college_sirius_sochi = SiriusCollege()
print('Sirius College:')
college_sirius_sochi.get_work_practice().get_practice(college_sirius_sochi.get_technology())

tech_college_sochi = UsualCollege()
print('\nUsual College:')
tech_college_sochi.get_work_practice().get_practice(tech_college_sochi.get_technology())