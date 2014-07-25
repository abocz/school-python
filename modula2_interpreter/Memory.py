

class Memory(object):
	mem = [0]*52
	
	@staticmethod
	def fetch(self, ch):
		return mem[self.get_index(ch)]
	
	@staticmethod
	def store(self, ch, value):
		mem[self.get_index(ch)] = value
		
	@staticmethod	
	def get_index(self, ch):
		if not ch.isalpha:
			raise ValueError("Invalid variable name")
		if ch.islower:
			index = ord(ch) - ord('a');
		else:
			index = ord(ch) - ord('A') + 26
		return index
	
		
