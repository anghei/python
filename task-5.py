"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь
"""

from faker import Faker
from uuid import uuid4
import json


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

    @staticmethod
    def add(item_id=uuid4()):
        printer_dict['id'] = item_id
        printer_model = input(f'Add model of printer: ')
        printer_dict['model'] = printer_model
        printer_qty = input(f'Add quantity of printers: ')
        printer_dict['qty'] = int(printer_qty)
        print(printer_dict)

    def option(self, item_id=uuid4()):
        pass


class Scanner(Equipment):

    @staticmethod
    def add(item_id=uuid4()):
        scanner_dict['id'] = item_id
        scanner_model = input(f'Add model of scanner: ')
        scanner_dict['model'] = scanner_model
        scanner_qty = input(f'Add quantity of scanners: ')
        scanner_dict['qty'] = int(scanner_qty)
        print(scanner_dict)


class Copier(Equipment):

    @staticmethod
    def add(item_id=uuid4()):
        copier_dict['id'] = item_id
        copier_model = input(f'Add model of copier: ')
        copier_dict['model'] = copier_model
        copier_qty = input(f'Add quantity of copiers: ')
        copier_dict['qty'] = int(copier_qty)
        print(copier_dict)

        # def create_json():
        #     with open("storage_db.json", "w+") as file:
        #         data = json.load(file)
        #         data.update(copier_dict)
        #         file.seek(0)
        #         json.dump(data, file)
        # return create_json()


class Agg:
    @staticmethod
    def summarize():
        pass


Copier.add()
print(copier_dict.get('id'))
