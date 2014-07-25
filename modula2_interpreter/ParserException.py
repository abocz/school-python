

class ParserException(Exception):
	
	def __init__(self, message):
		if not message:
			raise ValueError("No message for ParserException")
		self.message = message
	
	def __str__(self):
		return self.message
		