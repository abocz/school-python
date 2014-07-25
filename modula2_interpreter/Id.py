from Memory import Memory

class Id():

	def __init__(self, ch):
		if not ch:
			raise ValueError("Expected character in Id")
		self.ch = ch
		
	def get_char(self):
		return self.ch
		
	def evaluate(self):
		Memory.fetch(self.ch)
		
	def set_value(self, value):
		Memory.store(self.ch, value)
	