countries = ['ru', 'us']

#при инстанцировании 
#при добавление страны нам не нужно менять метод, мы его добавляем, расширяя 

class College:
    def __init__(self, name: str, location: str, country: str):
        self.name, self.location = name, location
        
    #можно было бы добавить страну в колледж, но мы создадим отдельный cls метод
    @classmethod
    def create_us_college(cls, name: str, location: str):
        college = cls(name, location)
        setattr(college, 'level', 'bachelor')
        return college

    @classmethod
    def create_ru_college(cls, name: str, location: str):
        college = cls(name, location)
        college.level = 'specialist'
        return college

sirius_college = College.create_ru_college('sirius', 'sirius')
print(sirius_college.level)
us_college = College.create_us_college_('us')