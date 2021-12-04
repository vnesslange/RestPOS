import requests
from tkinter import *
from tkinter import ttk
import sqlite3
import DatabaseService
import json

root = Tk()
root.title("Main Screen")
root.geometry("1195x700")
order_screen_frame = Frame(root)
order_screen_frame.grid(row=1, column=0, columnspan=3, rowspan=49)
order_screen_scroll = Scrollbar(order_screen_frame, orient=VERTICAL)
order_screen = Listbox(order_screen_frame, height=30, width=50, yscrollcommand=order_screen_scroll.set)
order_screen.grid(row=2, column=0, sticky=N + S + W, columnspan=3, rowspan=48)
menu_screen = Frame(root)
menu_screen.grid(row=8, column=3, columnspan=5, rowspan=49, sticky=N + E + S + W)
order_screen_scroll.config(command=order_screen.yview)
order_screen_scroll.grid(row=2, column=4)
menu_screen.pack_propagate(0)

order_list = []
order_number = 0
total = 0
root.config(background="#ced3db")
menu_screen.config(background="#ced3db")
order_screen.config()

order_label = Label(root, text="Order Number:" + str(order_number))
order_label.grid(row=4, column=3, sticky=N)
total_label = Label(root, text="Total:" + "")
total_label.grid(row=49, column=2, sticky=N)

payload = {}

with open("Modify.txt") as file:
    for line in file:
        command, description = line.strip().split(None, 1)
        payload[command] = description.strip()


def get_modify_values():
    clear_menu_screen()
    value = payload.values()
    value = list(value)
    get_string = value[0].split(",")
    for record in get_string:
        create_modify_button(record)


def create_modify_button(record):
    name = Button(menu_screen, padx=40, pady=20, bd=3, text=record, width=8,
                  command=lambda: insert_modify(record))
    name.pack()


def insert_modify(record):
    order_screen.insert(END, record)



def clear_menu_screen():
    """Function clears menu screen when you switch to a new menu"""
    for menu_buttons in menu_screen.winfo_children():
        menu_buttons.destroy()


def clear_order_screen():
    order_screen.delete(0, END)
    global total
    total = 0


def new_order():
    clear_order_screen()
    clear_total_and_order()
    get_next_order_number()
    order_label.config(text="Order Number:" + str(order_number))


def mgmt():
    """Takes you to screen to access the database for CRUD"""
    clear_menu_screen()
    import mgmt
    Button(menu_screen, padx=40, pady=20, text="Edit Entrees", width=8, command=mgmt.edit_entrees).pack()
    Button(menu_screen, padx=40, pady=20, text="Edit Apps", width=8, command=mgmt.edit_apps).pack()
    Button(menu_screen, padx=40, pady=20, text="Edit Drinks", width=8, command=mgmt.edit_drinks).pack()
    Button(menu_screen, padx=40, pady=20, text="Edit Desserts", width=8, command=mgmt.edit_desserts).pack()


def create_temp_button(record, number):
    """Function creates temp buttons for the screen you are on"""
    number = Button(menu_screen, padx=40, pady=20, bd=3, text=record[0], width=8,
                    command=lambda: order(record[0], record[1]))
    number.pack()


def query_db(statement):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute(statement)
    records = c.fetchall()
    for record in records:
        create_temp_button(record, record[2])

    conn.commit()
    conn.close()


def entrees_screen():
    clear_menu_screen()
    query_db("SELECT *, oid FROM entrees")


def apps_screen():
    clear_menu_screen()
    query_db("SELECT *, oid FROM apps")


def drinks_screen():
    clear_menu_screen()
    query_db("SELECT *, oid FROM drinks")


def desserts_screen():
    clear_menu_screen()
    query_db("SELECT *, oid FROM desserts")


def order(name, price):
    """Function places clicked buttons onto list screen"""
    order_screen.insert(END, name)
    order_screen.insert(END, str(price))
    order_tup = (name, price)
    record_order(order_tup)


def record_order(order_tup):
    order_list.append(order_tup)
    global total
    for i in order_list:
        total += i[1]

    total_label.config(text="Total:" + str(total))


def send_order():
    for i in order_list:
        order_insert(order_number, i[0], i[1])
    order_list.clear()
    order_screen.delete(0, END)
    clear_total_and_order()


def increment_order_number():
    global order_number
    order_number += 1


def clear_total_and_order():
    order_list.clear()
    total_label.config(text="Total:")
    order_label.config(text="Order Number:")


def order_insert(order_number, item_name, price):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders VALUES(:order_number, :item_name, :price)",
              {"order_number": order_number,
               "item_name": item_name,
               "price": price
               }
              )
    conn.commit()
    conn.close()


def create_temp_lookup_button(record, number):
    """Function creates temp buttons for the screen you are on"""
    number = Button(menu_screen, padx=40, pady=20, bd=3, text=record[0], width=8,
                    command=lambda: order_look_up_display(record)).pack()


def order_look_up():
    """Function populates buttons for desserts screen"""
    clear_menu_screen()
    clear_order_screen()
    clear_total_and_order()
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT order_number FROM orders")
    records = c.fetchall()
    for record in records:
        create_temp_lookup_button(record, record[0])

    conn.commit()
    conn.close()


def order_look_up_display(record):
    global order_number
    order_number = record[0]
    clear_menu_screen()
    clear_order_screen()
    clear_total_and_order()
    order_label.config(text="Order Number:" + str(order_number))
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *  FROM orders WHERE order_number = " + str(order_number))
    records = c.fetchall()
    for record in records:
        order(record[1], record[2])
    order_list.clear()


def delete_order_item():
    order_screen.delete(ANCHOR)


def void_order_item():
    item_to_void = order_screen.get(ANCHOR)
    global order_number
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT oid, item_name FROM orders WHERE order_number = " + str(order_number))
    records = c.fetchall()
    for record in records:
        if item_to_void == record[1]:
            item_to_void = record[0]
        perform_void(item_to_void, order)

    conn.commit()
    conn.close()


def perform_void(item_to_void, order):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("DELETE from orders WHERE oid= " + str(item_to_void))
    conn.commit()
    conn.close()
    refresh_display_after_void(order)


def refresh_display_after_void(order_number):
    clear_menu_screen()
    clear_order_screen()
    clear_total_and_order()
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *  FROM orders WHERE order_number = " + str(order_number))
    records = c.fetchall()
    for record in records:
        order(record[1], record[2])
    order_list.clear()
    conn.commit()
    conn.close()


def write_memo():
    clear_menu_screen()
    memo_text = Entry(menu_screen, width=30)
    memo_text.pack()
    Button(menu_screen, text="Enter Memo", command=lambda: place_memo_on_order_screen(memo_text.get())).pack()


def place_memo_on_order_screen(memo_text):
    order_screen.insert(END, memo_text)


def payment_screen():
    clear_menu_screen()
    payment_screen_buttons()


def payment_screen_buttons():
    cash = Button(menu_screen, text="Cash", padx=40, pady=20, width=8, command=lambda: process_payment("cash")).pack()
    card = Button(menu_screen, text="Credit", padx=40, pady=20, width=8, command=lambda: process_payment("card")).pack()
    split = Button(menu_screen, text="Split Payment", padx=40, pady=20, width=8, command="split_payments").pack()


def process_payment(payment_type):
    global order_number
    global total
    payments_insert(order_number, payment_type, total)
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("DELETE FROM orders WHERE order_number = " + str(order_number))
    c.execute("SELECT * FROM payments")
    records = c.fetchall()
    for record in records:
        print(record)
    conn.commit()
    conn.close()


def payments_insert(order_number, payment, total):
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("INSERT INTO payments VALUES(:order_number, :payment, :total)",
              {"order_number": order_number,
               "payment": payment,
               "total": total
               }
              )
    conn.commit()
    conn.close()

    clear_total_and_order()
    Label(order_screen, text="Payment Successful")
    return


def get_next_order_number():
    global order_number
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT MAX(order_number) FROM orders")
    records = c.fetchall()
    for record in records:
        if record[0] is not None:
            current_order_number = record[0] + 1
            order_number = current_order_number
        else:
            order_number = 1
    conn.commit()
    conn.close()


# Defining Permanent Buttons


memo = Button(root, text="Memo", width=5, padx=40, pady=20, command=write_memo)
modify = Button(root, text="Modify", width=5, padx=40, pady=20, command=get_modify_values)
fast_screen = Button(root, text="Fast Screen", width=5, padx=40, pady=20, command="")
apps = Button(root, text="Apps", width=7, padx=40, pady=20, command=apps_screen)
entrees = Button(root, text="Entrees", width=7, padx=40, pady=20, command=entrees_screen)
drinks = Button(root, text="Drinks", width=7, padx=40, pady=20, command=drinks_screen)
desserts = Button(root, text="Desserts", width=7, padx=40, pady=20, command=desserts_screen)
mgmt_screen = Button(root, text="MGMT", width=7, padx=40, pady=20, command=mgmt)
delete = Button(root, text="Delete", width=8, padx=40, pady=20, command=delete_order_item)
void = Button(root, text="Void", width=8, padx=40, pady=20, background="#7a8aa3", foreground="#171e29",
              command=void_order_item)
look_up = Button(root, text="Look Up", width=8, padx=40, pady=20, command=order_look_up)
new = Button(root, text="New Order", width=8, padx=40, pady=20, command=new_order)
payment = Button(root, text="Payment", background="#7a8aa3", padx=40, pady=20, foreground="#171e29", width=8,
                 command=payment_screen)
send = Button(root, text="Send", padx=40, pady=20, activebackground="#7a8aa3", foreground="#171e29", width=8,
              command=send_order)

# Placing buttons on screen

memo.grid(row=0, column=0, sticky=N + E + S + W)
modify.grid(row=0, column=1, sticky=N + E + S + W)
fast_screen.grid(row=0, column=2, sticky=N + E + S + W)
apps.grid(row=0, column=3, sticky=N + E + S + W)
entrees.grid(row=0, column=4, sticky=N + E + S + W)
drinks.grid(row=0, column=5, sticky=N + E + S + W)
desserts.grid(row=0, column=6, sticky=N + E + S + W)
mgmt_screen.grid(row=0, column=7, sticky=N + E + S + W)
delete.grid(row=51, column=0, sticky=N + E + S + W)
void.grid(row=51, column=1, sticky=N + E + S + W)
payment.grid(row=52, column=2, sticky=N + E + S + W)
look_up.grid(row=52, column=0, sticky=N + E + S + W)
new.grid(row=52, column=1, sticky=N + E + S + W)
send.grid(row=51, column=2, sticky=N + E + S + W)

root.mainloop()
