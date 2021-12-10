from sqlite3 import *


def dataTable():
    con = connect("./book.db")
    cursery = con.cursor()
    cursery.execute(
        "CREATE TABLE IF NOT EXISTS bookTBL(id INTEGER PRIMARY KEY ,Title text,Author text, year INTEGER , isbn INTEGER )")
    con.commit()
    con.close()


def insert(title, author, year, isbn):
    con = connect("./book.db")
    cursery = con.cursor()
    cursery.execute(
        "INSERT INTO bookTBL VALUES (NULL , ? , ? , ? , ?)", (title, author, year, isbn))
    con.commit()
    con.close()


def view():
    con = connect("./book.db")
    cursery = con.cursor()
    cursery.execute(
        "SELECT * FROM bookTBL")
    rows = cursery.fetchall()
    con.close()
    return rows


def search(title="", author="", year="", isbn=""):
    con = connect("./book.db")
    cursery = con.cursor()
    cursery.execute(
        "SELECT * FROM bookTBL WHERE Title LIKE ? OR Author LIKE ? OR year LIKE ? OR isbn LIKE ?",
        (title, author, year, isbn))
    rows = cursery.fetchall()
    con.close()
    return rows


def delete(id):
    con = connect("./book.db")
    cursery = con.cursor()
    cursery.execute(
        "DELETE FROM bookTBL WHERE id =  ?", (id,))
    con.commit()
    con.close()


def update(id, title, author, year, isbn):
    con = connect("./book.db")
    cursery = con.cursor()
    cursery.execute(
        "UPDATE bookTBL SET Title = ? , Author = ? , year =? , isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    con.commit()
    con.close()


dataTable()
