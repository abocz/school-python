class Token(object):

	def __init__(self, lexeme, rowNumber, columnNumber, tok):
		if lexeme is None or 0:
			raise ValueError("invalid lexeme")
		if rowNumber <= 0:
			raise ValueError("invalid row number")
		if columnNumber <= 0:
			raise ValueError("invalid column number")
		self.lexeme = lexeme
		self.rowNumber = rowNumber
		self.columnNumber = columnNumber
		self.tok = tok

	def getLexeme(self):
		return self.lexeme

	def getRowNum(self):
		return self.rowNumber

	def getColumnNum(self):
		return self.columnNumber

	def getTokenType(self):
		return self.tok