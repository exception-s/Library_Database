import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta


def generate_loans(num_loans=100):
    loans = []
    for _ in range(num_loans):
        user_id = random.choice(user_ids)
        book_id = random.choice(book_ids)
        loan_date = fake.date_between(start_date='-2y', end_date='today')
        return_date = loan_date + timedelta(days=random.randint(7, 30)) if random.random() > 0.1 else None  # 10% книг не возвращены
        loans.append((book_id, user_id, loan_date, return_date))
    return loans


fake = Faker()
conn = psycopg2.connect(
    dbname="dbstud",
    user="itmo408321_2024",
    password="************",
    host="146.185.211.205",
    port="5432"
)
cur = conn.cursor()
cur.execute("SELECT user_id FROM Users")
user_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT book_id FROM Books")
book_ids = [row[0] for row in cur.fetchall()]
loans_data = generate_loans()
conn.close()
