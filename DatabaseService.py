import sqlite3


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


