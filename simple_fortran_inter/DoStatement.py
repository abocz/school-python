from Statement import Statement

class DoStatement(Statement):
	def __init__(self, var, first, last, sList):
		if not var:
			raise ValueError("invalid variable argument")
		if first > last:
			raise ValueError("invalid loop indices argument")
		if not sList:
			raise ValueError("null statement list argument")
		self.var = var
		self.first = first
		self.last = last
		self.sList = sList
		
	def execute(self):
		self.var.setValue(self.first)
		while self.var.evaluate() <= self.last:
			self.sList.execute()
			self.var.setValue(self.var.evaluate() + 1)