from Expression import Expression


class BinaryExpression(Expression):
	ArithmeticOperator = ['ADD_OP', 'SUB_OP', 'MUL_OP', 'DIV_OP']

	def __init__(self, op, expr1, expr2):
		if not expr1 or not expr2:
			raise ValueError("null binary expression argument")
		self.op = op
		self.expr1 = expr1
		self.expr2 = expr2

	def evaluate(self):
		if self.op == BinaryExpression.ArithmeticOperator[0]:
			value = int(self.expr1.evaluate()) + int(self.expr2.evaluate())
		elif self.op == BinaryExpression.ArithmeticOperator[1]:
			value = int(self.expr1.evaluate()) - int(self.expr2.evaluate())
		elif self.op == BinaryExpression.ArithmeticOperator[2]:
			value = int(self.expr1.evaluate()) * int(self.expr2.evaluate())
		elif self.op == BinaryExpression.ArithmeticOperator[3]:
			value = int(self.expr1.evaluate()) / int(self.expr2.evaluate())
		else:
			raise ValueError("Invalid Arithmetic Operator in Binary Expression")
		return value