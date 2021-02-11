
"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь
"""

from faker import Faker
import sqlite3
from time import sleep

conn = sqlite3.connect('storage.db')
# cursor = conn.cursor()


equipment_dict = {}
printer_dict = {}
copier_dict = {}
scanner_dict = {}
department = ['Accounting', 'IT', 'HR', 'Support']


class SQL:

    @staticmethod
    def insert(connection, data):
        cursor = conn.cursor()

        cursor.execute("INSERT INTO equipment(name, brand, color, qty, price) VALUES(?, ?, ?, ?, ?)", data)
        conn.commit()

    @staticmethod
    def fetch(connection: object, sql_query: object) -> object:
        cursor = conn.cursor()

        cursor.execute(sql_query)
        rows = cursor.fetchall()
        for row in rows:
            return row[0]

    @staticmethod
    def info():
        conn = sqlite3.connect('storage.db')

        cursor = conn.cursor()

        sql_query = 'SELECT * FROM equipment'
        cursor.execute(sql_query)
        conn.commit()

class Storage:
    def __init__(self, place='A01', shipper=Faker().company):
        self.place = place
        self.shipper = shipper

    @staticmethod
    def info():
        sql_printer_qty = "SELECT SUM([qty]) FROM equipment WHERE [name] == 'Printer'"
        sql_copier_qty = "SELECT SUM([qty]) FROM equipment WHERE [name] == 'Copier'"
        sql_scanner_qty = "SELECT SUM([qty]) FROM equipment WHERE [name] == 'Scanner'"
        print('=' * 33)
        print(f'Warehouse store follow equipment:\n' \
              f'=================================\n'
              f'1. Printers - {SQL.fetch(connection=conn, sql_query=sql_printer_qty)}\n'
              f'\t Shipper are {Faker().company()}\n'
              f'2. Scanners - {SQL.fetch(connection=conn, sql_query=sql_scanner_qty)}\n'
              f'\t Shipper are {Faker().company()}\n'
              f'3. Copiers - {SQL.fetch(connection=conn, sql_query=sql_copier_qty)}\n'
              f'\t Shipper are {Faker().company()}')
        # sql_fetch(
        #     connection=conn,
        #     sql_query='SELECT SUM([qty]) FROM equipment WHERE [name] == "Printer"')

    @staticmethod
    def transfer():

        sql_printer_qty = "SELECT SUM([qty]) FROM equipment WHERE [name] == 'Printer'"
        sql_copier_qty = "SELECT SUM([qty]) FROM equipment WHERE [name] == 'Copier'"
        sql_scanner_qty = "SELECT SUM([qty]) FROM equipment WHERE [name] == 'Scanner'"

        printer_qty = SQL.fetch(connection=conn, sql_query=sql_printer_qty)
        scanner_qty = SQL.fetch(connection=conn, sql_query=sql_scanner_qty)
        copier_qty = SQL.fetch(connection=conn, sql_query=sql_copier_qty)

        print('1. '+department[0]+'\n2. ' + department[1]+'\n3. '+ department[2]+'\n4. ' + department[3])
        # print('-' * 12)
        choose_dep = input('Choose department to transfer office equipment: ')
        if choose_dep == '1':
            print(f'--> {department[0]} department chosen')
        elif choose_dep == '2':
            print(f'--> {department[1]} department chosen')
        elif choose_dep == '3':
            print(f'--> {department[2]} department chosen')
        elif choose_dep == '4':
            print(f'--> {department[3]} department chosen')
        sleep(1.0)
        print(f'\n\u2666 In storage we have now follow equipment:\n' \
              f'1. Printers - {printer_qty}\n'
              f'2. Scanners - {scanner_qty}\n'
              f'3. Copiers - {copier_qty}')
        choose_equip = input('Choose what equipment you want transfer to department: ')
        if choose_equip == '1':
            choose_qty = input(f'How many printers you want to transfer: ')
            if int(choose_qty) <= printer_qty:
                print(f'Ok! We transfer equipment in {department[int(choose_dep) - 1]}')
            else:
                print('Please, check quantity of equipment one more time! Wrong input!')
        if choose_equip == '2':
            choose_qty = input(f'How many scanners you want to transfer: ')
            if int(choose_qty) <= scanner_qty:
                print(f'Ok! We transfer equipment in {department[int(choose_dep) - 1]}')
            else:
                print('Please, check quantity of equipment one more time! Wrong input!')
        if choose_equip == '3':
            choose_qty = input(f'How many copier you want to transfer: ')
            if int(choose_qty) <= copier_qty:
                print(f'Ok! We transfer equipment in {department[int(choose_dep) - 1]}')
            else:
                print('Please, check quantity of equipment one more time! Wrong input!')


class Equipment:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price


class Printer(Equipment):

    @staticmethod
    def add():
        printer_dict['name'] = 'Printer'
        printer_model = input(f'Add brand of printer: ')
        printer_dict['brand'] = printer_model.title()
        printer_color = input(f'Add color of printer: ')
        printer_dict['color'] = printer_color.title()
        printer_qty = input(f'Add quantity of printers: ')
        printer_dict['qty'] = int(printer_qty)
        printer_price = input(f'Add price of printer: ')
        printer_dict['price'] = int(printer_price)

        data = (printer_dict.get('name'), printer_dict.get('brand'), printer_dict.get('color'), printer_dict.get('qty'),
                printer_dict.get('price'))

        SQL.insert(connection=conn, data=data)


class Scanner(Equipment):

    @staticmethod
    def add():
        scanner_dict['name'] = 'Scanner'
        scanner_model = input(f'Add brand of scanner: ')
        scanner_dict['brand'] = scanner_model.title()
        scanner_color = input(f'Add color of scanner: ')
        scanner_dict['color'] = scanner_color.title()
        scanner_qty = input(f'Add quantity of scanners: ')
        scanner_dict['qty'] = int(scanner_qty)
        scanner_price = input(f'Add price of scanner: ')
        scanner_dict['price'] = int(scanner_price)

        data = (scanner_dict.get('name'), scanner_dict.get('brand'), scanner_dict.get('color'), scanner_dict.get('qty'),
                scanner_dict.get('price'))

        SQL.insert(connection=conn, data=data)


class Copier(Equipment):

    @staticmethod
    def add():
        copier_dict['name'] = 'Copier'
        copier_model = input(f'Add brand of copier: ')
        copier_dict['brand'] = copier_model.title()
        copier_color = input(f'Add color of copier: ')
        copier_dict['color'] = copier_color.title()
        copier_qty = input(f'Add quantity of copiers: ')
        copier_dict['qty'] = int(copier_qty)
        copier_price = input(f'Add price of copier: ')
        copier_dict['price'] = int(copier_price)
        # print(copier_dict)

        data = (copier_dict.get('name'), copier_dict.get('brand'), copier_dict.get('color'), copier_dict.get('qty'),
                copier_dict.get('price'))

        SQL.insert(connection=conn, data=data)


Scanner.add()

# print(copier_dict.get('id'))
