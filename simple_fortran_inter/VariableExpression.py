from Expression import Expression
from Memory import Memory


class VariableExpression(Expression):
	def __init__(self, var):
		self.var = var
	def evaluate(self):
		return Memory.fetch(self.var)
	def setValue(self, value):
		Memory.store(self.var, value)