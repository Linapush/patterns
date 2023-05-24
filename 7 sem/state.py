# паттерн Состояния

from abc import ABC, abstractmethod

class StudentState(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass

    @abstractmethod
    def sleep(self) -> str:
        pass

    @abstractmethod
    def learn(self) -> str:
        pass

class EatingStudentState(StudentState):
    def eat(self) -> str:
        return 'already eating'
    
    def sleep(self) -> str:
        return 'cannot sleep rn, but syrely will after'
    
    def learn(self) -> str:
        return 'watching some educational videous'
    
class SleepingStudentEating(StudentState):
    def eat(self) -> str:
        return 'cannot eat rn, but will surely wake up hungry'
    
    def sleep(self) -> str:
        return 'already sleeping'
    
    def learn(self) -> str:
        return 'our students are learning new even while they are sleeping'
    
class LearningStudentState(StudentState):
    def eat(self) -> str:
        'should not be distracted with food while studying'

    def sleep(self) -> str:
        'should not fall asleep while studying'

    def learn(self) -> str:
        return ''

class Student:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, new_state: StudentState):
        if isinstance(new_state, StudentState):
            print(f'{self.name} current state changed to {}')
            self.state = new_state

    state = property(get_state, set_state)

    def sleep(self):
        self._execute('sleep')

    def eat(self):
        self._execute('eat')

    def learn(self):
        self._execute('learn')

    def execute(self, action: str):
        print(f'{self.name}: {getattr(self.state, action)()}')

kirill = Student('Kirill', LearningStudentState())
kirill.learn()
kirill.sleep()
kirill.eat()
kirill.state = EatingStudentState()
kirill.study()
kirill.eat()
kirill.state = SleepingStudentEating
kirill.sleep()
kirill.learn()

# в выводе в зависимости от предыдущего состояния студента будет возвращать новое
# + паттерна, как будто меняется сам объект, но на самом