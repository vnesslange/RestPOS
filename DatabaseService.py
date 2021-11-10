import sqlite3
import main


conn = sqlite3.connect('restPOS.db')

c = conn.cursor()

c.execute("INSERT INTO entrees")