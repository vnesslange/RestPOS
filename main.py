import requests
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Main Screen")

order_screen = Listbox(root, height=30, width=45)
order_screen.grid(row=1, column=0, columnspan=3, rowspan=49)
menu_screen = PanedWindow(root,  height=30, width=45)
menu_screen.grid(row=1, column=3, columnspan=4, rowspan=49)


def memo():
    return


# Defining Buttons

memo = Button(root, text="Memo", padx=40, pady=20, command=memo)
modify = Button(root, text="Modify", padx=40, pady=20, command=memo)
fast_screen = Button(root, text="Fast Screen", padx=40, pady=20, command=memo)
apps = Button(root, text="Apps", padx=40, pady=20, command=memo)
entrees = Button(root, text="Entrees", padx=40, pady=20, command=memo)
drinks = Button(root, text="Drinks", padx=40, pady=20, command=memo)
desserts = Button(root, text="Desserts", padx=40, pady=20, command=memo)
mgmt = Button(root, text="MGMT", padx=40, pady=20, command=memo)
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
mgmt.grid(row=0, column=7)
delete.grid(row=51, column=0)
void.grid(row=51, column=1)
payment.grid(row=51, column=2)
look_up.grid(row=52, column=0)
new.grid(row=52, column=1)

root.mainloop()
