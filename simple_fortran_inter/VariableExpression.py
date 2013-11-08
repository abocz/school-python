from Expression import Expression
from Memory import Memory


class VariableExpression(Expression):
	def __init__(self, var):
		self.var = var

	def evaluate(self):
		print("begin eval")
		return Memory.fetch(self.var)

	def setValue(self, value):
		print("set value started!")
		print(self.var)
		print(value)
		Memory.store(self.var, value)