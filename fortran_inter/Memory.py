from string import ascii_lowercase


class Memory(object):
	mem = []
	letters = list(ascii_lowercase)
	for x in range(len(letters)):
		mem.append(0)

	def store(self, var, value):
		if not var.isalpha:
			raise ValueError("invalid memory access")
		var.lower()
		self.mem[ord(var)-ord('a')] = value

	def fetch(self, var):
		if not var.isalpha:
			raise ValueError("invalid memory access")
		var.lower()
		return self.mem[ord(var)-ord('a')]