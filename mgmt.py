import requests
from tkinter import *
from tkinter import ttk
import sqlite3
import DatabaseService


def clear(name, price):
    """Function Clears Text Boxes for Forms"""
    name.delete(0, END)
    price.delete(0, END)


def clear_for_delete(number):
    """Function to Clear Delete text box"""
    number.delete(0, END)


# Functions for Entrees

def edit_entrees():
    root = Tk()
    root.title("Edit Entrees")
    root.geometry("200x300")
    Button(root, padx=40, pady=20, text="Add Entree", command=add_entrees).pack()
    Button(root, padx=40, pady=20, text="Edit Entree", command=update_entrees).pack()
    Button(root, padx=40, pady=20, text="Delete Entree", command=delete_entrees).pack()
    Button(root, padx=40, pady=20, text="Display all Entree", command=display_entrees).pack()


def add_entrees():
    root = Tk()
    root.title("Entrees")
    root.geometry("400x250")
    entree_name = Entry(root, width=30)
    entree_name.grid(row=0, column=1)
    entree_name_label = Label(root, text="Enter Name:")
    entree_name_label.grid(row=0, column=0)
    entree_price = Entry(root, width=30)
    entree_price.grid(row=1, column=1)
    entree_price_label = Label(root, text="Enter Price:")
    entree_price_label.grid(row=1, column=0)

    entree_submit = Button(root, text="Add Entree",
                           command=lambda: [entree_records(entree_name.get(), entree_price.get()),
                                            clear(entree_name, entree_price)])
    entree_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)


def delete_entrees():
    root = Tk()
    root.title("Entrees")
    root.geometry("400x250")
    delete_entree_num = Entry(root, width=30)
    delete_entree_num.grid(row=0, column=1)
    delete_entree_num_label = Label(root, text="Enter ID number of Entree:")
    delete_entree_num_label.grid(row=0, column=0)

    delete_entree_submit = Button(root, text="Delete Entree",
                                  command=lambda: [delete_entrees_records(delete_entree_num.get()),
                                                   clear_for_delete(delete_entree_num)])
    delete_entree_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def delete_entrees_records(delete_entree_num):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("DELETE from entrees WHERE oid= " + delete_entree_num)

    conn.commit()
    conn.close()


def update_entrees():
    root = Tk()
    root.title("Entrees")
    root.geometry("400x250")
    update_entree_num = Entry(root, width=30)
    update_entree_num.grid(row=0, column=1)
    update_entree_num_label = Label(root, text="Enter ID number of Entree:")
    update_entree_num_label.grid(row=0, column=0)

    update_entree_submit = Button(root, text="Get Entree",
                                  command=lambda: update_entrees_records(update_entree_num.get()))

    update_entree_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def update_entrees_records(update_entree_num):
    root = Tk()
    root.title("Entrees")
    root.geometry("400x250")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT * from entrees WHERE oid= " + update_entree_num)
    records = c.fetchall()
    for record in records:
        entree_name = Entry(root, width=30)
        entree_name.grid(row=0, column=1)
        entree_name.insert(0, record[0])
        entree_name_label = Label(root, text="Enter Name:")
        entree_name_label.grid(row=0, column=0)
        entree_price = Entry(root, width=30)
        entree_price.grid(row=1, column=1)
        entree_price.insert(0, record[1])
        entree_price_label = Label(root, text="Enter Price:")
        entree_price_label.grid(row=1, column=0)

    entree_submit = Button(root, text="Add Entree",
                           command=lambda: [
                               update_entrees_in_table(entree_name.get(), entree_price.get(), update_entree_num),
                               clear(entree_name, entree_price)])
    entree_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)

    conn.commit()
    conn.close()


def update_entrees_in_table(entree_name, price, record_id):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""UPDATE entrees SET
            entree_name = :entree_name,
            price = :price

            WHERE oid = :oid""",
              {
                  "entree_name": entree_name,
                  "price": price,

                  "oid": record_id

              })

    conn.commit()
    conn.close()


def entree_records(entree_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO entrees VALUES(:entree_name, :price)",
              {"entree_name": entree_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def display_entrees():
    root = Tk()
    root.title("Entrees")
    root.geometry("500x500")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM entrees")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[2]) + "  name: " + str(record[0]) + "  price: " + str(record[1]) + "\n"

    display_text = Label(root, text=print_records, font=("Arial", 20)).pack()

    conn.commit()
    conn.close()


# Functions for Apps

def edit_apps():
    root = Tk()
    root.title("Edit Apps")
    root.geometry("200x300")
    Button(root, padx=40, pady=20, text="Add Apps", command=add_apps).pack()
    Button(root, padx=40, pady=20, text="Edit Apps", command=update_apps).pack()
    Button(root, padx=40, pady=20, text="Delete Apps", command=delete_apps).pack()
    Button(root, padx=40, pady=20, text="Display all Apps", command=display_apps).pack()


def add_apps():
    root = Tk()
    root.title("APPs")
    root.geometry("400x250")
    app_name = Entry(root, width=30)
    app_name.grid(row=0, column=1)
    app_name_label = Label(root, text="Enter Name:")
    app_name_label.grid(row=0, column=0)
    app_price = Entry(root, width=30)
    app_price.grid(row=1, column=1)
    app_price_label = Label(root, text="Enter Price:")
    app_price_label.grid(row=1, column=0)

    app_submit = Button(root, text="Add App",
                        command=lambda: [app_records(app_name.get(), app_price.get()), clear(app_name, app_price)])
    app_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)


def app_records(app_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO apps VALUES(:app_name, :price)",
              {"app_name": app_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def delete_apps():
    root = Tk()
    root.title("Apps")
    root.geometry("400x250")
    delete_apps_num = Entry(root, width=30)
    delete_apps_num.grid(row=0, column=1)
    delete_apps_num_label = Label(root, text="Enter ID number of App:")
    delete_apps_num_label.grid(row=0, column=0)

    apps_entree_submit = Button(root, text="Delete App",
                                command=lambda: [delete_apps_records(delete_apps_num.get()),
                                                 clear_for_delete(delete_apps_num)])
    apps_entree_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def delete_apps_records(delete_apps_num):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("DELETE from apps WHERE oid= " + delete_apps_num)

    conn.commit()
    conn.close()


def update_apps():
    root = Tk()
    root.title("Apps")
    root.geometry("400x250")
    update_apps_num = Entry(root, width=30)
    update_apps_num.grid(row=0, column=1)
    update_apps_num_label = Label(root, text="Enter ID number of App:")
    update_apps_num_label.grid(row=0, column=0)

    update_apps_submit = Button(root, text="Get App",
                                command=lambda: update_apps_records(update_apps_num.get()))

    update_apps_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def update_apps_records(update_apps_num):
    root = Tk()
    root.title("Apps")
    root.geometry("400x250")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT * from apps WHERE oid= " + update_apps_num)
    records = c.fetchall()
    for record in records:
        apps_name = Entry(root, width=30)
        apps_name.grid(row=0, column=1)
        apps_name.insert(0, record[0])
        apps_name_label = Label(root, text="Enter Name:")
        apps_name_label.grid(row=0, column=0)
        apps_price = Entry(root, width=30)
        apps_price.grid(row=1, column=1)
        apps_price.insert(0, record[1])
        apps_price_label = Label(root, text="Enter Price:")
        apps_price_label.grid(row=1, column=0)

    apps_submit = Button(root, text="Add Apps",
                         command=lambda: [update_apps_in_table(apps_name.get(), apps_price.get(), update_apps_num),
                                          clear(apps_name, apps_price)])
    apps_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)

    conn.commit()
    conn.close()


def update_apps_in_table(apps_name, price, record_id):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""UPDATE apps SET
            app_name = :app_name,
            price = :price

            WHERE oid = :oid""",
              {
                  "app_name": apps_name,
                  "price": price,

                  "oid": record_id

              })

    conn.commit()
    conn.close()


def display_apps():
    root = Tk()
    root.title("Apps")
    root.geometry("500x500")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM apps")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[2]) + "  name: " + str(record[0]) + "  price: " + str(record[1]) + "\n"

    display_text = Label(root, text=print_records, font=("Arial", 20)).pack()

    conn.commit()
    conn.close()


# Functions for Drinks

def edit_drinks():
    root = Tk()
    root.title("Edit Drinks")
    root.geometry("200x300")
    Button(root, padx=40, pady=20, text="Add Drinks", command=add_drinks).pack()
    Button(root, padx=40, pady=20, text="Edit Drinks", command=update_drinks).pack()
    Button(root, padx=40, pady=20, text="Delete Drinks", command=delete_drinks).pack()
    Button(root, padx=40, pady=20, text="Display all Drinks", command=display_drinks).pack()


def add_drinks():
    root = Tk()
    root.title("Drinks")
    root.geometry("400x250")
    drinks_name = Entry(root, width=30)
    drinks_name.grid(row=0, column=1)
    drinks_name_label = Label(root, text="Enter Name:")
    drinks_name_label.grid(row=0, column=0)
    drinks_price = Entry(root, width=30)
    drinks_price.grid(row=1, column=1)
    drinks_price_label = Label(root, text="Enter Price:")
    drinks_price_label.grid(row=1, column=0)

    drinks_submit = Button(root, text="Add Drinks",
                           command=lambda: [drinks_records(drinks_name.get(), drinks_price.get()),
                                            clear(drinks_name, drinks_price)])
    drinks_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)


def drinks_records(drinks_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO drinks VALUES(:drinks_name, :price)",
              {"drinks_name": drinks_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def delete_drinks():
    root = Tk()
    root.title("Drinks")
    root.geometry("400x250")
    delete_drinks_num = Entry(root, width=30)
    delete_drinks_num.grid(row=0, column=1)
    delete_drinks_num_label = Label(root, text="Enter ID number of Drink:")
    delete_drinks_num_label.grid(row=0, column=0)

    delete_drinks_submit = Button(root, text="Delete Drink",
                                  command=lambda: [delete_drinks_records(delete_drinks_num.get()),
                                                   clear_for_delete(delete_drinks_num)])
    delete_drinks_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def delete_drinks_records(delete_drinks_num):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("DELETE from drinks WHERE oid= " + delete_drinks_num)

    conn.commit()
    conn.close()


def update_drinks():
    root = Tk()
    root.title("Drinks")
    root.geometry("400x250")
    update_drinks_num = Entry(root, width=30)
    update_drinks_num.grid(row=0, column=1)
    update_drinks_num_label = Label(root, text="Enter ID number of Drinks:")
    update_drinks_num_label.grid(row=0, column=0)

    update_drinks_submit = Button(root, text="Get Drink",
                                  command=lambda: update_drinks_records(update_drinks_num.get()))

    update_drinks_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def update_drinks_records(update_drinks_num):
    root = Tk()
    root.title("Drinks")
    root.geometry("400x250")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT * from drinks WHERE oid= " + update_drinks_num)
    records = c.fetchall()
    for record in records:
        drinks_name = Entry(root, width=30)
        drinks_name.grid(row=0, column=1)
        drinks_name.insert(0, record[0])
        drinks_name_label = Label(root, text="Enter Name:")
        drinks_name_label.grid(row=0, column=0)
        drinks_price = Entry(root, width=30)
        drinks_price.grid(row=1, column=1)
        drinks_price.insert(0, record[1])
        drinks_price_label = Label(root, text="Enter Price:")
        drinks_price_label.grid(row=1, column=0)

    drinks_submit = Button(root, text="Update Drink",
                           command=lambda: [
                               update_drinks_in_table(drinks_name.get(), drinks_price.get(), update_drinks_num),
                               clear(drinks_name, drinks_price)])
    drinks_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)

    conn.commit()
    conn.close()


def update_drinks_in_table(drinks_name, price, record_id):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""UPDATE drinks SET
            drinks_name = :drinks_name_name,
            price = :price

            WHERE oid = :oid""",
              {
                  "drinks_name_name": drinks_name,
                  "price": price,

                  "oid": record_id

              })

    conn.commit()
    conn.close()


def display_drinks():
    root = Tk()
    root.title("Drinks")
    root.geometry("500x500")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM drinks")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[2]) + "  name: " + str(record[0]) + "  price: " + str(record[1]) + "\n"

    display_text = Label(root, text=print_records, font=("Arial", 20)).pack()

    conn.commit()
    conn.close()


# Functions for Desserts

def edit_desserts():
    root = Tk()
    root.title("Edit Desserts")
    root.geometry("200x300")
    Button(root, padx=40, pady=20, text="Add Desserts", command=add_desserts).pack()
    Button(root, padx=40, pady=20, text="Edit Desserts", command=update_desserts).pack()
    Button(root, padx=40, pady=20, text="Delete Desserts", command=delete_desserts).pack()
    Button(root, padx=40, pady=20, text="Display all Desserts", command=display_desserts).pack()


def add_desserts():
    root = Tk()
    root.title("Desserts")
    root.geometry("400x250")
    desserts_name = Entry(root, width=30)
    desserts_name.grid(row=0, column=1)
    desserts_name_label = Label(root, text="Enter Name:")
    desserts_name_label.grid(row=0, column=0)
    desserts_price = Entry(root, width=30)
    desserts_price.grid(row=1, column=1)
    desserts_price_label = Label(root, text="Enter Price:")
    desserts_price_label.grid(row=1, column=0)

    desserts_submit = Button(root, text="Add Desserts",
                             command=lambda: [desserts_records(desserts_name.get(), desserts_price.get()),
                                              clear(desserts_name, desserts_price)])
    desserts_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)


def desserts_records(desserts_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO desserts VALUES(:desserts_name, :price)",
              {"desserts_name": desserts_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def delete_desserts():
    root = Tk()
    root.title("Desserts")
    root.geometry("400x250")
    delete_desserts_num = Entry(root, width=30)
    delete_desserts_num.grid(row=0, column=1)
    delete_desserts_num_label = Label(root, text="Enter ID number of Dessert:")
    delete_desserts_num_label.grid(row=0, column=0)

    delete_desserts_submit = Button(root, text="Delete Dessert",
                                    command=lambda: [delete_desserts_records(delete_desserts_num.get()),
                                                     clear_for_delete(delete_desserts_num)])
    delete_desserts_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def delete_desserts_records(delete_desserts_num):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("DELETE from desserts WHERE oid= " + delete_desserts_num)

    conn.commit()
    conn.close()


def update_desserts():
    root = Tk()
    root.title("Desserts")
    root.geometry("400x250")
    update_desserts_num = Entry(root, width=30)
    update_desserts_num.grid(row=0, column=1)
    update_desserts_num_label = Label(root, text="Enter ID number of Dessert:")
    update_desserts_num_label.grid(row=0, column=0)

    update_desserts_submit = Button(root, text="Get Dessert",
                                    command=lambda: update_desserts_records(update_desserts_num.get()))

    update_desserts_submit.grid(row=2, columnspan=2, pady=10, padx=10, ipadx=100)


def update_desserts_records(update_desserts_num):
    root = Tk()
    root.title("Desserts")
    root.geometry("400x250")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT * from desserts WHERE oid= " + update_desserts_num)
    records = c.fetchall()
    for record in records:
        desserts_name = Entry(root, width=30)
        desserts_name.grid(row=0, column=1)
        desserts_name.insert(0, record[0])
        desserts_name_label = Label(root, text="Enter Name:")
        desserts_name_label.grid(row=0, column=0)
        desserts_price = Entry(root, width=30)
        desserts_price.grid(row=1, column=1)
        desserts_price.insert(0, record[1])
        desserts_price_label = Label(root, text="Enter Price:")
        desserts_price_label.grid(row=1, column=0)

    desserts_submit = Button(root, text="Update Dessert",
                             command=lambda: [update_desserts_in_table(desserts_name.get(), desserts_price.get(),
                                                                       update_desserts_num),
                                              clear(desserts_name, desserts_price)])
    desserts_submit.grid(row=3, columnspan=2, pady=10, padx=10, ipadx=100)

    conn.commit()
    conn.close()

def update_desserts_in_table(desserts_name, price, record_id):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("""UPDATE desserts SET
            drinks_name = :desserts_name,
            price = :price

            WHERE oid = :oid""",
              {
                  "desserts_name": desserts_name,
                  "price": price,

                  "oid": record_id

              })

    conn.commit()
    conn.close()





def display_desserts():
    root = Tk()
    root.title("Desserts")
    root.geometry("500x500")
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM desserts")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[2]) + "  name: " + str(record[0]) + "  price: " + str(record[1]) + "\n"

    display_text = Label(root, text=print_records, font=("Arial", 20)).pack()

    conn.commit()
    conn.close()
