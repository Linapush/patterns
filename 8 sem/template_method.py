# Танцы состоят из движений

from abc import ABC, abstractmethod

class Dancer(ABC):
    directions = {'forward': (1, 0),
                'backward': (-1, 0),
                'left': (0, -1), 
                'right': (0, 1),
                'in_place': (0, 0)
    }

    @abstractmethod
    def move(self) -> None:
        pass

    def __init__(self, name: str):
        self.name = name
        self.position = 0, 0
        self.angle = 0 

    def _step(self, direction: str, angle: int): #внутренний метод
        if direction not in self.directions:
            raise Exception('unknown direction')
        
        if self.angle > 0 and direction != 'in_place':
            new_dir_index = self.dirs.index(direction) + self.angle // 90
            new_dir_index = new_dir_index % len(self.dirs)
            direction = self.dirs[new_dir_index]


        
        to_add = self.directions[direction]
        self.position = self.position[0] + to_add[0], self.position[1] + to_add
        new_angle = self.angle += angle

    def _step_right(self, direction: str, angle: int = 0): #внутренний метод
        self._step(direction, angle)
        
    def _step_left(self, direction: str, angle: int = 0): #внутренний метод      
        self._step(direction, angle)
        
class WaltzDancer(Dancer):
    def move(self) -> None:
        #левая пошла
        self._step_left('forward', 90)
        self._step_right('in_place', 90)
        self._step_left('in_place')

        #прававя пошла
        self._step_right('backward', 90)
        self._step_left('in_place', 90)
        self._step_right('in_place')
        print(f'После цикла танцор {self.name} оказался в {self.position} под углом {self.angle}')

vlad = WaltzDancer('Vlad')
vlad.move()