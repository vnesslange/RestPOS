import requests
from tkinter import *
from tkinter import ttk
import sqlite3
import DatabaseService


# Functions for Entrees

def edit_entrees():
    root = Tk()
    root.title("Edit Entrees")
    root.geometry("200x300")
    Button(root, padx=40, pady=20, text="Add Entree", command="").pack()
    Button(root, padx=40, pady=20, text="Edit Entree", command="").pack()
    Button(root, padx=40, pady=20, text="Delete Entree", command="").pack()
    Button(root, padx=40, pady=20, text="Display all Entree", command=display_entrees).pack()


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
    Button(root, padx=40, pady=20, text="Add Apps", command="").pack()
    Button(root, padx=40, pady=20, text="Edit Apps", command="").pack()
    Button(root, padx=40, pady=20, text="Delete Apps", command="").pack()
    Button(root, padx=40, pady=20, text="Display all Apps", command=display_apps).pack()


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
    Button(root, padx=40, pady=20, text="Add Drinks", command="").pack()
    Button(root, padx=40, pady=20, text="Edit Drinks", command="").pack()
    Button(root, padx=40, pady=20, text="Delete Drinks", command="").pack()
    Button(root, padx=40, pady=20, text="Display all Drinks", command=display_drinks).pack()


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
    Button(root, padx=40, pady=20, text="Add Desserts", command="").pack()
    Button(root, padx=40, pady=20, text="Edit Desserts", command="").pack()
    Button(root, padx=40, pady=20, text="Delete Desserts", command="").pack()
    Button(root, padx=40, pady=20, text="Display all Desserts", command=display_desserts).pack()


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
