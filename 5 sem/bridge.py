# Мост между страницей и рендером
# Renderer: get: str -> str
# UpperRenderer: method get: str -> str
# TittleRenderee: method get: str -> str
# Page: content: str, renderee: Renderer

from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def get(text: str) -> str:
        pass

class UpperRenderer(Renderer):
    @staticmethod
    def get(text: str) -> str:
        return text.upper()
    
class TittleRenderer(Renderer):
    @staticmethod
    def get(text: str) -> str:
        return text.capitalize()

# принимает объекты
# заранее продумана архитектура
# 
class Page:
    def __init__(self, content: str, renderer: Renderer):
        self.content, self.renderer = content, renderer

    def get_content(self):
        return self.renderer.get(self.__content)

    def set_content(self, new_content: str):
        if isinstance(new_content, str):
            self.__content = new_content

    content = property(get_content, set_content)
        
    
main_page = Page('hello', UpperRenderer)
print(main_page.content)
main_page.content = 1
print(main_page.content)

# Цель адаптера - устранить несовместимость между двумя существующими интерфейсами. При разработке адаптера не учитывается, как эти интерфейсы реализованы и то, как они могут независимо развиваться в будущем. Он должен лишь обеспе­чить совместную работу двух независимо разработанных классов, так чтобы ни один из них не пришлось переделывать.
# Цель моста - разделять абстракцию и реализацию так, чтобы они могли изменяться независимо