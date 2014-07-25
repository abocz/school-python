from Statement import Statement

class WhileStatement(Statement):
	
	def __init__(self, expr, ss):
		if not expr:
			raise ValueError("Expected expression in WhileStatement")
		if not ss:
			raise ValueError("Expected expression in WhileStatement")
		self.expr = expr
		self.ss = ss
		
	def execute(self):
		while self.expr.evaluate():
			self.ss.execute()