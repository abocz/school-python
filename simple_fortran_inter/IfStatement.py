from Statement import Statement


class IfStatement(Statement):

	def __init__(self, expr, sList1, sList2):
		if not expr:
			raise ValueError("null exception argument")
		if not sList1 or not sList2:
			raise ValueError("null expression argument")
		self.expr = expr
		self.sList1 = sList1
		self.sList2 = sList2

	def execute(self):
		if self.expr.evaluate:
			self.sList1.execute()
		else:
			self.sList2.execute()