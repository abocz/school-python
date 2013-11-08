from Expression import Expression


class ConstantExpression(Expression):

	def __init__(self, value):
		self.value = value

	def evaluate(self):
		return self.value