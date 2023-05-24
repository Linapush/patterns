# Заместитель, предоставляет доступ

from abc import ABC
from typing import Tuple

class Page(ABC):
    allowed_gids: Tuple[int]

    def __init__(self, content: str):
        self.content = content

class MainPage(Page):
    allowed_gids = (1, 2, 3)

class AdminPage(Page):
    allowed_gids = (1,)

class User:
    def __init__(self, name: str, gids: Tuple[int]):
        self.name, self.gids = name, gids
        #self.id = User.id
        self.id = self.__class__.id
        self.__class__.id += 1

class PermitProxy:
    @staticmethod
    def get_page_content(page: Page, user: User):
        #1 !!!!!
        # for gid in user.gids:
        #     if gid in page.allowed_gids:
        #         return page.content
        # return 'You do not have access to this page content.'
    
        #2 !!!! Основы (set, intersection)
        if set(user.gids) & set(page.allowed_gids):
            return page.content
        return f'403: You do not have acces to this page content, {user.name}'

alina = User('Alina', 1)
arina = User('Arina', 2)
main_page = MainPage('Hello y\'all!')
admin_page = AdminPage('Only admin sees it.')
print(PermitProxy.get_page_content(main_page, arina))
print(PermitProxy.get_page_content(admin_page, alina))
print(PermitProxy.get_page_content(admin_page, alina))