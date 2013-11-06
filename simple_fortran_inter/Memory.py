from string import ascii_lowercase
letters = list(ascii_lowercase)
class Memory(object):
	def store(self, var, value):
		if not var.isalpha:
			raise ValueError("invalid memory access")
		var.lower()
		# NOT FINISHED
	def fetch(self, var):
		if not var.isalpha:
			raise ValueError("invalid memory access")
		var.lower()
		return #NOT FINISHED