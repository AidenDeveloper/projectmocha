import sqlite3
from account import Account
conn = sqlite3.connect('accounts.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#    username text,
#    password text,
#    points integer
#)""")

#c.execute("INSERT INTO employees VALUES ('AidenDev', 'finngaming123', 150)")

conn.commit()

user = input("Enter username")
passs = input("Enter password")
#emp_1 = Account(username, password, 150)
a = c.execute("SELECT * FROM employees WHERE username='{}' AND password='{}'".format(user,passs))
emptylist = '[]'
if a == emptylist:
    print("Invalid")
else:
    print(c.fetchall())    

conn.commit()

conn.close()