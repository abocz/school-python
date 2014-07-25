from Statement import Statement


class IfStatement(Statement):

	def __init__(self, expr, cb1, cb2):
		if not expr:
			raise ValueError("Invalid expression in IfStatement")
		if not ss1 or ss2:
			raise ValueError("Invalid StatementSequence in IfStatement")
		self.expr = expr
		self.ss1 = ss1
		self.ss2 = ss2

	def execute(self):
		if self.expr.evaluate():
			self.ss1.execute()
		else:
			self.ss2.execute()
