from LexicalException import LexicalException
from Token import Token
from TokenType import TokenType


class LexicalAnalyzer(object):

	def __init__(self, file_name):
		if not file_name or len(file_name) < 1:
			raise ValueError("Invalid file in LexicalAnalyzer")
		self.token_list = []
		line_num = 0
		print("prefile")
		inputFile = open(file_name)
		print("postfile")
		lines = [line.strip() for line in inputFile]
		#ASSURE SOLUTION WORKS
		while line_num < len(lines)+1:
			self.process_line(lines[line_num-1], line_num)
			line_num += 1
		inputFile.close()
		self.token_list.append(Token(line_num, 1, "EOS", TokenType.EOS_TOK))

	def process_line(self, line, line_num):
		assert line is not None
		assert line_num > 0
		index = 0
		index = self.skip_white_space(line, index)
		while index < len(line):
			lexeme = self.get_lexeme(line, index)
			tokType = self.determine_token_type(lexeme, line_num, index)
			tok = Token(line_num, column_num+1, lexeme, tokType)
			self.token_list.append(tok)
			index += len(lexeme)
			index = self.skip_white_space(line, index)

	def determine_token_type(self, lexeme, line_num, index):
		assert lexeme is not None
		assert line_num > 0
		assert index >= 0
		if lexeme[0].isalpha():
			if len(lexeme) is 1:
				tokType = TokenType.ID_TOK
			elif lexeme == "IF":
				tokType = TokenType.IF_TOK
			elif lexeme == "UNTIL":
				tokType = TokenType.UNTIL_TOK
			elif lexeme == "THEN":
				tokType = TokenType.THEN_TOK
			elif lexeme == "ELSE":
				tokType = TokenType.ELSE_TOK
			elif lexeme == "END":
				tokType = TokenType.END_TOK
			elif lexeme == "PrintInt":
				tokType = TokenType.PRINT_TOK
			elif lexeme == "BEGIN":
				tokType = TokenType.BEGIN_TOK
			elif lexeme == "WHILE":
				tokType = TokenType.WHILE_TOK
			elif lexeme == "DO":
				tokType = TokenType.DO_TOK
			elif lexeme == "BEGIN":
				tokType = TokenType.BEGIN_TOK
			elif lexeme == "MODULE":
					tokType = TokenType.MODULE_TOK
			else:
				raise LexicalException("Invalid aplhabetic lexeme")
		elif lexeme[0].isdigit():
			if self.all_digits(lexeme):
				tokType = TokenType.LIT_INT
			else:
				raise LexicalException("Invalid digit lexeme")
		elif lexeme == ":=":
			tokType = TokenType.ASSIGN_OP
		elif lexeme == "+":
			tokType = TokenType.ADD_TOK
		elif lexeme == "-":
			tokType = TokenType.SUB_TOK
		elif lexeme == "*":
			tokType = TokenType.MUL_TOK
		elif lexeme == "/":
			tokType = TokenType.DIV_TOK
		elif lexeme == "==":
			tokType = TokenType.EQ_TOK
		elif lexeme == "#":
			tokType = TokenType.NE_TOK
		elif lexeme == "<":
			tokType = TokenType.LT_TOK
		elif lexeme == "<=":
			tokType = TokenType.LE_TOK
		elif lexeme == ">":
			tokType = TokenType.GT_TOK
		elif lexeme == ">=":
			tokType = TokenType.GE_TOK
		elif lexeme == ".":
				tokType = TokenType.PERIOD_TOK
		elif lexeme == "(":
				tokType = TokenType.LEFT_PAREN_TOK
		elif lexeme == ")":
				tokType = TokenType.RIGHT_PAREN_TOK
		elif lexeme == ";":
			tokType = TokenType.SEMI_COLON_TOK
		else:
			raise LexicalException("Invalid special character lexeme")
		return tokType

	def all_digits(self, s):
		assert s is not None
		i = 0
		while (i < (len(s))) and (s[i].isdigit()):
			i += 1
		return i == len(s)

	def get_lexeme(self, line, index):
		assert line is not None
		assert len(line) > 0 
		assert index >= 0 and index < len(line)
		i = index
		while (i < len(line)) and (not line[i].isspace()):
			i +=1
		return line[index:i]

	def skip_white_space(self, line, index):
		assert line is not None
		assert index >= 0
		while (index < len(line)) and (line[index].isspace()):
			index += 1
		return index

	def get_next_token(self):
		if not self.more_tokens():
			raise LexicalException("No more tokens")
		return self.token_list.pop(0)

	def more_tokens(self):
		if len(self.token_list)>0:
			return True
		else:
			return False

	def get_lookahead_token(self):
		if not self.more_tokens():
			raise LexicalException("No more tokens")
		return self.token_list[0]
