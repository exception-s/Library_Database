import psycopg2

from BooksParsing import books_data
from UsersGenerator import users_data


def insert_books_data(conn, books_data):
    cur = conn.cursor()
    for book in books_data:
        cur.execute("""
        INSERT INTO Authors (name) VALUES (%s) returning author_id;
        """, (book['author'],))
        author_id = cur.fetchone()[0]

        cur.execute("""
        INSERT INTO Books (title, author_id, published_date) VALUES (%s, %s, %s);
        """, (book['title'], author_id, book['published_date']))
    conn.commit()
    cur.close()


def insert_users_data(conn, users_data):
    cur = conn.cursor()
    for user in users_data:
        cur.execute("""
        INSERT INTO Users (name, email) VALUES (%s, %s);
        """, (user['name'], user['email']))
    conn.commit()
    cur.close()


conn = psycopg2.connect(
    dbname="dbstud",
    user="itmo408321_2024",
    password="itmo408321",
    host="146.185.211.205",
    port="5432"
)

insert_books_data(conn, books_data)
insert_users_data(conn, users_data)


conn.close()
