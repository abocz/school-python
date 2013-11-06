from Expression import Expression

class BinaryExpression(Expression):
	ArithmeticOperator = ['ADD_OP', 'SUB_OP', 'MUL_OP', 'DIV_OP']
	def __init__(self, op, expr1, expr2):
		if not expr1 or not expr2:
			raise ValueError("null expression argument")
		self.op = op
		self.expr1 = expr1
		self.expr2 = expr2
	def evaluate(self):
		value = 0
		if self.op is 'ADD_OP':
			return self.expr1.evaluate() + self.expr2.evaluate()
		elif self.op is 'SUB_OP':
			return self.expr1.evaluate() - self.expr2.evaluate()
		elif self.op is 'MUL_OP':
			return self.expr1.evaluate() * self.expr2.evaluate()
		else:
			return self.expr1.evaluate() / self.expr2.evaluate()