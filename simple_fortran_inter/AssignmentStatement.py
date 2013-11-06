from Statement import Statement

class AssignmentStatement(Statement):
	def __init__(self, var, expr):
		if not expr:
			raise ValueError("invalid expression argument")
		if not var:
			raise ValueError("invalid variable argument")
		self.expr = expr
		self.var = var
		
	def execute(self):
		self.var.setValue(self.expr.evaluate())