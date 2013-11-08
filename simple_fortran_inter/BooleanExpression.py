class BooleanExpression(object):
	RelativeOperator = ['LE', 'LT', 'GE', 'GT', 'EQ', 'NE']

	def __init__(self, op, expr1, expr2):
		if not expr1 or not expr2:
			raise ValueError("null boolean expression argument")
		self.op = op
		self.expr1 = expr1
		self.expr2 = expr2

	def evaluate(self):
		if self.op == BooleanExpression.RelativeOperator[0]:
			return self.expr1.evaluate() <= self.expr2.evaluate()
		elif self.op == BooleanExpression.RelativeOperator[1]:
			return self.expr1.evaluate() < self.expr2.evaluate()
		elif self.op == BooleanExpression.RelativeOperator[2]:
			return self.expr1.evaluate() >= self.expr2.evaluate()
		elif self.op == BooleanExpression.RelativeOperator[3]:
			return self.expr1.evaluate() > self.expr2.evaluate()
		elif self.op == BooleanExpression.RelativeOperator[4]:
			return self.expr1.evaluate() == self.expr2.evaluate()
		elif self.op == BooleanExpression.RelativeOperator[5]:
			return self.expr1.evaluate() != self.expr2.evaluate()
		else:
			raise ValueError("Invalid boolean expression error")