import requests


def get_books_data(subject='mathematics', limit=100):
    url = f'https://openlibrary.org/subjects/{subject}.json?limit={limit}'
    response = requests.get(url)
    data = response.json()
    books = []
    for book in data['works']:
        book_info = {
            'title': book['title'],
            'author': book['authors'][0]['name'],
            'published_date': book.get('first_publish_year', 'Unknown')
        }
        books.append(book_info)
    return books


books_data = get_books_data()
for book in books_data:
    print(book)
