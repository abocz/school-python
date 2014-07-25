from Statement import Statement


class RepeatStatement(Statement):
	
	def __init__(self, expr, ss):
		if not expr:
			raise ValueError("Expected expression in Repeat Statement")
		if not ss:
			raise ValueError("Expected statement sequence in Repeat Statement")
		self.expr = epxr
		self.ss = ss
		
	def execute(self):
		while True:
			self.ss.execute()
			if self.expr.evaluate():
				break