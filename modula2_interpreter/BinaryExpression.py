from Expression import Expression

class BinaryExpression(Expression):
	def __init__(self, op, expr1, epxr2):
		if not op:
			raise ValueError("Invalid operator in BinaryExpression")
		if not expr1 or not expr2:
			raise ValueError("Invalid expression in BinaryExpression")
		self.op = op
		self.expr1 = expr1
		self.expr2 = expr2

	def evaluate(self):
		if self.op == ArithmeticOperator.ADD_OP:
			value = int(self.expr1.evaluate()) + int(self.expr2.evaluate())
		elif self.op == ArithmeticOperator.SUB_OP:
			value = int(self.expr1.evaluate()) - int(self.expr2.evaluate())
		elif self.op == ArithmeticOperator.MUL_OP:
			value = int(self.expr1.evaluate()) * int(self.expr2.evaluate())
		elif self.op == ArithmeticOperator.DIV_OP:
			value = int(self.expr1.evaluate()) / int(self.expr2.evaluate())
		else:
			raise ValueError("Invalid Arithmetic op")
		return value
