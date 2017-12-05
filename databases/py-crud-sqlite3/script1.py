import sqlite3

def create_table():
    #1 connect to db
    connection=sqlite3.connect("lite.db")
    #2 create cursor object
    cursor=connection.cursor()
    #3 write SQL query
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #4 commit changes to db
    connection.commit()
    #5 close connection
    connection.close()

def insert(item, quantity, price):
    connection=sqlite3.connect("lite.db")
    cursor=connection.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    # use ? to avoid SQL injections
    connection.commit()
    connection.close()

def view():
    connection=sqlite3.connect("lite.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    connection.close()
    return rows

def update(quantity,price,item):
    connection=sqlite3.connect("lite.db")
    cursor=connection.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    connection.commit()
    connection.close()

def delete(item):
    connection=sqlite3.connect("lite.db")
    cursor=connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(item,))
    rows=cursor.fetchall()
    connection.commit()
    connection.close()

create_table()
insert('wine glass',1,1)
insert('coffee mug',10,1)
# delete('coffee mug')
update(22, 2,'wine glass')
print(view())
