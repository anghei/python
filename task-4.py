"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники
"""


from faker import Faker
from uuid import uuid4

equipment_dict = {}
printer_dict = {}
copier_dict = {}
scanner_dict = {}
department = ['Accounting', 'IT', 'HR', 'Support']


class Storage:
    def __init__(self, place='A01', shipper=Faker().company):
        self.place = place
        self.shipper = shipper


class Equipment:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price


class Printer(Equipment):
    def option(self, item_id=uuid4()):
        pass


class Scanner(Equipment):
    def option(self, item_id=uuid4()):
        pass


class Copier(Equipment):
    def option(self, item_id=uuid4()):
        pass


Storage.add()