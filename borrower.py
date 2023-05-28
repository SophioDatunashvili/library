from uuid import uuid4
from base_management import BaseManager


class Borrower:
	def __init__(self, first_name: str, last_name: str, mobile: str, address: str, email: str = None):
		self.id = str(uuid4())
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.mobile = mobile
		self.address = address
	
	def __str__(self):
		return f"{self.first_name} {self.last_name}"
	
	
class BorrowerManager(BaseManager):
	def __init__(self):
		super().__init__()
		self.borrowers = self.items
		
