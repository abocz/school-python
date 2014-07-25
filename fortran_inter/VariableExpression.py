from Expression import Expression
from Memory import Memory


class VariableExpression(Expression):

	def __init__(self, var):
		self.var = var
		self.testMemory = Memory()

	def evaluate(self):
		return self.testMemory.fetch(self.var)

	def setValue(self, value):
		self.testMemory.store(self.var, value)