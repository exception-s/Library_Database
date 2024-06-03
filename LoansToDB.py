import psycopg2
from LoansGenerator import loans_data


def insert_loans_data(conn, loans_data):
    cur = conn.cursor()
    for loan in loans_data:
        cur.execute("""
        INSERT INTO Loans (book_id, user_id, loan_date, return_date) VALUES (%s, %s, %s, %s);
        """, loan)
    conn.commit()
    cur.close()


conn = psycopg2.connect(
    dbname="dbstud",
    user="itmo408321_2024",
    password="************",
    host="146.185.211.205",
    port="5432"
)
insert_loans_data(conn, loans_data)
