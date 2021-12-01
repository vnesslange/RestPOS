import sqlite3
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def microservice():
    r = requests.get("http://127.0.0.1:5000/")
    microservice_dict = dict(r.json())
    values = list(microservice_dict.values())
    microservice_insert(values[0], values[1], values[2], values[3])
    return "Success"


def microservice_table():
    conn = sqlite3.connect('archive.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE archive (
                    StringBool int,
                    FloatBool int,
                    FloatProperty real,
                    StringProperty text
                    )""")
    conn.commit()
    conn.close()


def microservice_insert(StringBool, FloatBool, FloatProperty, StringProperty):
    conn = sqlite3.connect('archive.db')
    c = conn.cursor()
    c.execute("INSERT INTO archive VALUES(:StringBool, :FloatBool, :FloatProperty, :StringProperty)",
              {"StringBool": StringBool,
               "FloatBool": FloatBool,
               "FloatProperty": FloatProperty,
               "StringProperty": StringProperty
               }
              )
    conn.commit()
    conn.close()


def entree_table():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE entrees (
                    entree_name text,
                    price int
                    )""")
    conn.commit()
    conn.close()


def entree_insert(entree_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO entrees VALUES(:entree_name, :price)",
              {"entree_name": entree_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def query_entrees():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM entrees")
    print(c.fetchall())
    conn.commit()
    conn.close()


def apps_table():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE apps (
                    app_name text,
                    price int
                    )""")
    conn.commit()
    conn.close()


def apps_insert(app_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO apps VALUES(:app_name, :price)",
              {"app_name": app_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def query_apps():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM entrees")
    print(c.fetchall())
    conn.commit()
    conn.close()


def drinks_table():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE drinks (
                    drinks_name text,
                    price int
                    )""")
    conn.commit()
    conn.close()


def drinks_insert(drinks_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO drinks VALUES(:drinks_name, :price)",
              {"drinks_name": drinks_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def query_drinks():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM drinks")
    print(c.fetchall())
    conn.commit()
    conn.close()

def desserts_table():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE desserts (
                    desserts_name text,
                    price int
                    )""")
    conn.commit()
    conn.close()


def desserts_insert(desserts_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO desserts VALUES(:desserts_name, :price)",
              {"desserts_name": desserts_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def query_desserts():
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM desserts")
    print(c.fetchall())
    conn.commit()
    conn.close()



# app.run(port=8000)
"""
apps_insert("Spinach Dip", 8)
apps_insert("Onion Rings", 5)
apps_insert("Fries", 4)
apps_insert("Shrimp Cocktail", 14)
apps_insert("Wings", 10)
"""
"""
drinks_table()
drinks_insert("Margarita", 9)
drinks_insert("Beer", 6)
drinks_insert("Wine", 8)
"""
"""
desserts_table()
desserts_insert("Cheesecake", 6)
desserts_insert("Brownie", 5)
desserts_insert("Ice Cream", 3)
"""
