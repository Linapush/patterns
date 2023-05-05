# Билборд
#
#
#
from typing import List


class AdGetter:

    def __init__(self, ads: List[str]):
        self.ads = ads 

    # сделать так, чтобы список строк крутился

    def get_ad(self) -> str:
        ad = self.ads.pop()
        self.ads.insert(0, ad)
        return ad

class Visualizer:
    def __init__(self, width: int, height: int):
        self.__width, self.__height = None, None
        self.width = width
        self.height - height

    @staticmethod
    def checker(function):
        def new_f(self, value):
            if not isinstance(value, int) or value <= 0:
                raise Exception('value must be integer and greater than zero')
            function(self, value)
    @property
    def width(self):
        return self.__width
    
    #всегда устнаваливает ширину не меньше нуля
    @width.setter
    @checker
    def width(self, new_width: int):
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    def mat(self):
        return self.width, self.height

class Billboard:
    def __init__(self, ad_getter: AdGetter, visualizer: Visualizer):
        self.ad_getter, self.visualizer = ad_getter, visualizer

    def get_image(self):
        print(f'ad: {self.ad_getter.get_ad()} sized {self.visualizer.mat()}, ')
    
ad_getter = AdGetter(['Blend_a_med', '8 800 555 35 35', 'Mr.Propper'])
visualizer = Visualizer(1080, 720)
bb = Billboard(ad_getter, visualizer)

for _ in range(5):
    bb.get_image()