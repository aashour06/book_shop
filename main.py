import pandas as pd
import sqlite3

data=pd.read_csv("BooksDataset.csv")
df=pd.DataFrame(data)

conn=sqlite3.connect("database.db")
cur=conn.cursor()
df.dropna(subset=["Category"],inplace=True)
df.to_sql("Books", conn,if_exists="replace",index=False)

def display_all():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("""select Title from Books """)
    books=cur.fetchall()
    for book in books:
        print(book[0])

    conn.commit()
    conn.close()

def get_category():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    book_name=input("Enter book name : ")
    cur.execute("""select Category from Books where Title = ? """,(book_name,))
    book=cur.fetchone()
    if book :
        print(book[0])
    else:
        print("Doesnot exist")
    conn.commit()
    conn.close()

def get_price():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    book_name=input("Enter book name : ")
    cur.execute("""select Price from Books where Title = ? """,(book_name,))
    book=cur.fetchone()
    if book :
        print(book[0])
    else:
        print("Doesnot exist")
    conn.commit()
    conn.close()


display_all()
get_category()
get_price()