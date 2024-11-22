import requests
import json
import os
import random
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def fetch_books_data(query, api_key):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}&maxResults=40"
    response = requests.get(url)

    if response.status_code == 200:
        books_data = response.json().get('items', [])
        extracted_books = []
        
        for book_data in books_data:
            volume_info = book_data.get('volumeInfo', {})
            sale_info = book_data.get('saleInfo', {})
            price = 0
            
            if(sale_info.get('listPrice') is None):
                price = random.randint(100, 500)
            else:
                price = sale_info.get('listPrice').get('amount')

            book_info = {
                "id": book_data.get('id'),
                "title": volume_info.get('title'),
                "authors": volume_info.get('authors', []),
                "publisher": volume_info.get('publisher'),
                "publication_date": volume_info.get('publishedDate'),
                "categories": volume_info.get('categories', []),
                "description": volume_info.get('description', ''),
                "page_count": volume_info.get('pageCount', 0),
                "language": volume_info.get('language', ''),
                "cover_image_url": volume_info.get('imageLinks', {}).get('thumbnail', ''),
                "average_rating": volume_info.get('averageRating', 0),
                "price": price,
                "currency": "BRL"
            }

            extracted_books.append(book_info)

        
        filename = f"{query}_books.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(extracted_books, f, ensure_ascii=False, indent=4)
        
        print(f"Dados dos livros guardados em {filename}")
    else:
        print("Erro ao realizar a solicitude na API de Google Books")
        
categories = [
    "Fiction",
    "Non-Fiction",
    "Mystery & Thriller",
    "Science Fiction & Fantasy",
    "Romance",
    "Historical Fiction",
    "Biography & Memoir",
    "Self-Help",
    "Health & Wellness",
    "Science & Technology",
    "Travel & Adventure",
    "Poetry",
    "Young Adult",
    "Children's Books",
    "Graphic Novels & Comics",
    "Cooking & Food",
    "Religion & Spirituality",
    "Philosophy",
    "Art & Photography",
    "Business & Economics",
    "Politics & Social Sciences",
    "Education & Teaching",
    "Law & Legal Studies",
    "Hobbies & Crafts",
    "Parenting & Families"
]

for category in categories:
    fetch_books_data(category, api_key)
