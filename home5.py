# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private.
#     Соответственно, для получения значений этого атрибута нужно использовать методы get и set

# @classmethod можем обращаться к свойствам класса, которые объявлены по умолчанию и можем вызывать вот так
# доступ к свойствам класса через cls
# Programmer.print(skills)

# https://proproprogs.ru/python_oop/metody-klassa-classmethod-i-staticheskie-metody-staticmethod


from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def print_info(self):
        print('***********************')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        self.print_skills()

    @abstractmethod
    def print_skills(self):
        pass


class Programmer(Person):
    _skills = 'programming'

    def __init__(self, name, age, language):
        super().__init__(name, age)
        self._language = language

    def print_info(self):
        super().print_info()
        print(f'Language: {self._language}')

    @classmethod
    def print_skills(cls):
        print(f'Skills programmer: {cls._skills}')

    @classmethod
    def set_language(cls, language):
        cls._language = language


class Singer(Person):
    _skills = 'singing'

    def __init__(self, name, age, band):
        super().__init__(name, age)
        self._band = band

    def print_info(self):
        super().print_info()
        print(f'Band: {self.band}')

    @classmethod
    def print_skills(cls):
        print(f'Skills singer: {cls._skills}')

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        self._band = band


programmer = Programmer('Vladislav', 36, 'php')
singer = Singer('John', 37, 'Beatles')
my_list = [programmer, singer]
for item in my_list:
    item.print_info()

programmer.set_language('python')
singer.band = 'Prodigy'

for item in my_list:
    item.print_info()


Programmer.print_skills()
# print(programmer.__dict__)
