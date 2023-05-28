class BaseManager:
	def __init__(self):
		self.items = {}
		
	def create(self, item):
		self.items[item.id] = item
		
	def read(self, item_id):
		for item in self.items:
			if item == item_id:
				return self.items[item_id]
	
	def update(self, item_id, **kwargs):
		if item_id in self.items:
			item = self.items[item_id]
			for key, value in kwargs.items():
				item.key = value
			
	def delete(self, item_id):
		if item_id in self.items:
			del self.items[item_id]
	