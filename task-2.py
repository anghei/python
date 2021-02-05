from abc import ABC, abstractmethod


class ABSClass(ABC):
    @abstractmethod
    def textile(self):
        pass


class Clothes(ABSClass):
    def __init__(self, value=100):
        self.value = value

    @property
    def Coat_textile(self, value):
        pass

    @property
    def Costume_textile(self, value):
        pass

    @property
    def textile(self):
        return round((self.Coat_textile + self.Costume_textile), 1)


class Coat(Clothes):
    @property
    def textile(self):
        result = round(self.value / 6.5 + 0.5, 2)
        Clothes.Coat_textile = result
        return f'Для пошива пальто, {self.value} размера, необходима ткань в количестве {round(self.value / 6.5 + 0.5, 1)}'


class Costume(Clothes):
    @property
    def textile(self):
        result = round(2 * self.value + 0.3, 2)
        Clothes.Costume_textile = result
        return f'Для пошива костюма, с ростом {self.value} см, необходима ткань в количестве {round(2 * self.value + 0.3, 1)}'


general_cloth = Clothes()
my_coat = Coat(50)
print(my_coat.textile)
my_costume = Costume(180)
print(my_costume.textile)
print(f'Общий расход ткани составит при этом {general_cloth.textile}')
