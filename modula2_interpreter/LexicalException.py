

class LexicalException(Exception):
	def __init__(self):
		if not message:
			raise ValueError("null string argument")
		self.message = message

	def __str__(self):
		return self.message
