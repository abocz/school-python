

class Token(object):
	
	def __init__(self, row_number, column_number, lexeme, tok_type):
		self.row_number = row_number
		self.column_number = column_number
		self.lexeme = lexeme
		self.tok_type = tok_type
		
	def get_token_type(self):
		return self.tok_type
		
	def get_row_number(self):
		return self.row_number
		
	def get_column_number(self):
		return self.column_number
		
	def get_lexeme(self):
		return self.lexeme