import json
import random
from django.core.management.base import BaseCommand
from catalog.models import Book

class Command(BaseCommand):
    help = 'Popula a base de dados com os arquivos JSON de origem'
    
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='O arquivo JSON de origem')

    def handle(self, *args, **kwargs):
        
        filename = kwargs['filename']
        
        with open(filename, 'r', encoding='utf-8') as f:
            books_data = json.load(f)

            for data in books_data:
                stock = random.randint(1, 100)
                reviews = []
                categories = []
                
                if len(data.get('categories')) == 0:
                    categories = ['Others']
                else:
                    categories = data.get('categories')

                book = Book(
                    book_id=data.get('id'),
                    title=data.get('title'),
                    authors=data.get('authors'),
                    publisher=data.get('publisher'),
                    publication_date=data.get('publication_date'),
                    categories=categories,
                    description=data.get('description', ''),
                    page_count=data.get('page_count', 0),
                    language=data.get('language', ''),
                    price=data.get('price'),
                    currency=data.get('currency'),
                    stock=stock,
                    cover_image=data.get('cover_image_url'),
                    average_rating=data.get('average_rating', 0),
                    reviews=reviews
                )

                # Guardar em MongoDB
                book.save()
                self.stdout.write(self.style.SUCCESS(f"Livro '{book.title}' guardado com sucesso."))