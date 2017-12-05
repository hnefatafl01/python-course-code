import sqlite3

class Database:

    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
        self.con.commit()

    def create(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book values (NULL,?,?,?,?)", (title, author, year, isbn))
        self.con.commit()


    def read(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()

        return rows

    def search(self, title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()

        return rows

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?  WHERE (id=?)", (title,author,year,isbn,id))
        self.con.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE (id=?)", (id,))
        self.con.commit()

    def __del__(self):
        self.con.close()

# connectDB()
# create('The Hobbit','JRR Tolkien', 1937, 9780613536844)
# create('The Lord of The Rings','JRR Tolkien', 1955, 9788373191723)
# create('Peanuts Classics','Charles M. Schulz', 1970,9780030850783)
# update(5,'The Two Towers','JRR Tolkien', 1955, 9788373191723)
# delete(4)
# print(read())
# print(search(author="Charles M. Schulz"))
# update()
# delete()
