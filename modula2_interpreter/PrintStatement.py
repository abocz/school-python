from Statement import Statement

class PrintStatement(Statement):
	
	def __init__(self, expr):
		if not expr:
			raise ValueError("Null expression in Print Statement")
		self.expr = expr
		
	def execute(self):
		print(self.expr.evaluate())