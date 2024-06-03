import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="dbstud",
    user="itmo408321_2024",
    password="itmo408321",
    host="146.185.211.205",
    port="5432"
)

cur = conn.cursor()

# Пример запроса на получение списка всех книг
def get_all_books():
    cur.execute("SELECT * FROM Books")
    books = cur.fetchall()
    df_books = pd.DataFrame(books, columns=['book_id', 'title', 'author_id', 'published_date'])
    return df_books

# Пример запроса на поиск книг по автору
def get_books_by_author(author_name):
    query = """
    SELECT B.title FROM Books B
    JOIN Authors A ON B.author_id = A.author_id
    WHERE A.name = %s
    """
    cur.execute(query, (author_name,))
    books = cur.fetchall()
    df_books = pd.DataFrame(books, columns=['title'])
    return df_books


if __name__ == "__main__":
    print("All Books:")
    print(get_all_books())

    print("\nBooks by J.K. Rowling:")
    print(get_books_by_author('J.K. Rowling'))

cur.close()
conn.close()
