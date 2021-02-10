import sqlite3
import random

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS product(
                    item_id INT PRIMARY KEY, 
                    item_name TEXT, 
                    item_brand TEXT, 
                    item_color TEXT, 
                    item_qty INT);
""")


data = (1, 'printer', 'Canon', 'white', 5, 5000)

cursor.execute("INSERT INTO equipment VALUES(2, 'copier', 'hp', 'red', 10, 1000)")
conn.commit()

# cursor.execute("INSERT INTO product VALUES(lists[0], lists[1], lists[2], lists[3], lists[4])")
