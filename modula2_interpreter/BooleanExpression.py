from Expression import Expression
from RelationalOperator import RelationalOperator


class BooleanExpression(Expression):

	def __init__(self, op, expr1, expr2):
		if not op:
			raise ValueError("Invalid realtional operator in BooleanExpression")
		if not expr1 or expr2:
			raise ValueError("Invalid expression in BooleanExpression")
		self.op = op
		self.expr1 = expr1
		self.expr2 = expr2

	def evaluate(self):
		result = False
		if self.op == RelationalOperator.EQ_OP:
			result = int(self.expr1.evaluate()) == int(self.expr2.evaluate())
		if self.op == RelationalOperator.NE_OP:
			result = int(self.expr1.evaluate()) != int(self.expr2.evaluate())
		if self.op == RelationalOperator.LT_OP:
			result = int(self.expr1.evaluate()) < int(self.expr2.evaluate())
		if self.op == RelationalOperator.LE_OP:
			result = int(self.expr1.evaluate()) <= int(self.expr2.evaluate())
		if self.op == RelationalOperator.GT_OP:
			result = int(self.expr1.evaluate()) > int(self.expr2.evaluate())
		if self.op == RelationalOperator.GE_OP:
			result = int(self.expr1.evaluate()) >= int(self.expr2.evaluate())
		return result
