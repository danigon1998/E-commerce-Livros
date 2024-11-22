from django.shortcuts import render
from .models import Book

def book_list(request):
    category_filter = request.GET.get('category', None)
    
    categories = Book.objects.distinct('categories')
    
    if category_filter:
        books = Book.objects.filter(categories__in=[category_filter])
    else:
        books = Book.objects.all()
    
    limit = 20
    offset = int(request.GET.get('offset', 0))
    
    books = books[offset:offset+limit]
    
    context = {
        "books": books,
        "next_offset": offset + limit if offset + limit < books.count() else None,
        "categories": categories,
        "selected_category": category_filter
    }
    
    return render(request, 'book_list.html', context)


