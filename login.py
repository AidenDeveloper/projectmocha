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
funny = input("Type Register or Login: ")
if funny.lower() == "login":
    user = input("Enter username")
    passs = input("Enter password")
    a = f"SELECT username from employees WHERE username='{user}' AND password = '{passs}';"
    c.execute(a)
    if not c.fetchone():
        print("Invalid")
    else:
        print("gaming")  
#emp_1 = Account(username, password, 150)


  

conn.commit()

conn.close()