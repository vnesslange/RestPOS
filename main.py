import requests
from tkinter import *
from tkinter import ttk
import sqlite3
import DatabaseService

root = Tk()
root.title("Main Screen")
root.geometry("1100x700")

order_screen = Listbox(root, height=30, width=45)
order_screen.grid(row=1, column=0, columnspan=3, rowspan=49)
menu_screen = PanedWindow(root, height=30, width=45)
menu_screen.grid(row=1, column=3, columnspan=4, rowspan=49)


def memo():
    return


def clear_menu_screen():
    for menu_buttons in menu_screen.winfo_children():
        menu_buttons.destroy()


def mgmt():
    """Takes you to screen to access the data base for CRUD"""
    clear_menu_screen()
    import mgmt
    Button(menu_screen, padx=40, pady=20, text="Edit Entrees", command=mgmt.edit_entrees).pack()
    Button(menu_screen, padx=40, pady=20, text="Edit Apps", command=mgmt.edit_apps).pack()
    Button(menu_screen, padx=40, pady=20, text="Edit Drinks", command=mgmt.edit_drinks).pack()
    Button(menu_screen, padx=40, pady=20, text="Edit Desserts", command=mgmt.edit_desserts).pack()


def create_temp_button(record, number):
    """Function creates temp buttons for the screen you are on"""
    number = Button(menu_screen, padx=40, pady=20, text=record[0], command=lambda: order(record[0])).pack()


def entrees_screen():
    """Function populates buttons for entree screen"""
    clear_menu_screen()
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM entrees")
    records = c.fetchall()
    for record in records:
        create_temp_button(record, record[2])

    conn.commit()
    conn.close()


def apps_screen():
    """Function populates buttons for app screen"""
    clear_menu_screen()
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM apps")
    records = c.fetchall()
    for record in records:
        create_temp_button(record, record[2])

    conn.commit()
    conn.close()


def drinks_screen():
    """Function populates buttons for drinks screen"""
    clear_menu_screen()
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM drinks")
    records = c.fetchall()
    for record in records:
        create_temp_button(record, record[2])

    conn.commit()
    conn.close()


def desserts_screen():
    """Function populates buttons for desserts screen"""
    clear_menu_screen()
    conn = sqlite3.connect('restPOS.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM desserts")
    records = c.fetchall()
    for record in records:
        create_temp_button(record, record[2])

    conn.commit()
    conn.close()


def order(buttons):
    """Function places clicked buttons onto list screen"""
    order_screen.insert(0, buttons)


# Defining Permanent Buttons

memo = Button(root, text="Memo", padx=40, pady=20, command=memo)
modify = Button(root, text="Modify", padx=40, pady=20, command=memo)
fast_screen = Button(root, text="Fast Screen", padx=40, pady=20, command=memo)
apps = Button(root, text="Apps", padx=40, pady=20, command=apps_screen)
entrees = Button(root, text="Entrees", padx=40, pady=20, command=entrees_screen)
drinks = Button(root, text="Drinks", padx=40, pady=20, command=drinks_screen)
desserts = Button(root, text="Desserts", padx=40, pady=20, command=desserts_screen)
mgmt_screen = Button(root, text="MGMT", padx=40, pady=20, command=mgmt)
delete = Button(root, text="Delete", padx=40, pady=20, command=memo)
void = Button(root, text="Void", padx=40, pady=20, command=memo)
look_up = Button(root, text="Look Up", padx=40, pady=20, command=memo)
new = Button(root, text="New Order", padx=40, pady=20, command=memo)
payment = Button(root, text="Payment", padx=40, pady=20, command=memo)

# Placing buttons on screen

memo.grid(row=0, column=0)
modify.grid(row=0, column=1)
fast_screen.grid(row=0, column=2)
apps.grid(row=0, column=3)
entrees.grid(row=0, column=4)
drinks.grid(row=0, column=5)
desserts.grid(row=0, column=6)
mgmt_screen.grid(row=0, column=7)
delete.grid(row=51, column=0)
void.grid(row=51, column=1)
payment.grid(row=51, column=2)
look_up.grid(row=52, column=0)
new.grid(row=52, column=1)

root.mainloop()
