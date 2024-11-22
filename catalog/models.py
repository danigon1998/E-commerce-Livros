from mongoengine import Document, EmbeddedDocument, StringField, ListField, IntField, FloatField, URLField, DateTimeField, EmbeddedDocumentField

class Review(EmbeddedDocument):
    user_id = StringField(required=True)
    rating = FloatField(required=True, min_value=0, max_value=5)
    comment = StringField(required=False)
    review_date = DateTimeField(required=True)
    
class Book(Document):
    book_id = StringField(primary_key=True)
    title = StringField(required=True)
    authors = ListField(StringField())
    publisher = StringField()
    publication_date = StringField()
    categories = ListField(StringField(), required = True)
    description = StringField()
    page_count = IntField(required=True, min_value=1)
    language = StringField(required=True)
    price = FloatField()
    currency = StringField()
    stock = IntField(required=True, min_value=0, default=0)
    cover_image = URLField()
    average_rating = FloatField(min_value=0, max_value=5, default=2.5)
    reviews = ListField(EmbeddedDocumentField(Review))

    meta = {
        'collection': 'books' 
    }