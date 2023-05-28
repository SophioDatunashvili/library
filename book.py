from uuid import uuid4
from base_management import BaseManager


class Book:
	def __init__(self, title: str, author: str, ISBN: str, genre: str, publish_year: str):
		self.id = str(uuid4())[24:]
		self.title = title
		self.author = author
		self.ISBN = ISBN
		self.genre = genre
		self.publish_year = publish_year
	
	def __str__(self):
		return f"{self.title} by {self.author}"


class BookManager(BaseManager):
	def __init__(self):
		super().__init__()
		self.books = self.items


class SearchMethod:

	def __init__(self):
		self.filter = ["title", "author", "genre", "ISBN"]
		self.filtered_books = {}
		self.books = BookManager().books

	def filter_by(self, filter_by, filter_by_value):
		if filter_by in self.filter:
			for book_id, book in self.books.items():
				if book.filter_by == filter_by_value:
					self.filtered_books[book_id] = book
		return self.filtered_books

#
# b1 = Book(title="b1", author="me", ISBN="123", genre="comedy", publish_year="1999")
# b1_id = b1.id
# b2 = Book(title="b3", author="me", ISBN="123", genre="comedy", publish_year="1999")
# bm = BookManager()
# bm.create(b1)
# bm.create(b2)


