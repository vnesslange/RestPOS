import sqlite3
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def microservice():
    r = requests.get("http://127.0.0.1:5000/")
    microservice_dict = dict(r.json())
    values = list(microservice_dict.values())
    print(values)
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


app.run(port=8000)
