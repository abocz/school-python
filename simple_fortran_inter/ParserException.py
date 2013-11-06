class ParserException(Exception):
	def __init__(self, message, lineNum, columnNum):
		if not message:
			raise ValueError("null string argument")
		if lineNum <= 0:
			raise ValueError("invalid line argument")
		if column <= 0:
			raise ValueError("invalid column argument")
		self.message = message
		self.lineNum = lineNum
		self.columnNum = columnNum
	def __str__(self):
		return "{} at line number {} column number {}".format(self.message, self.lineNum, self.columnNum)