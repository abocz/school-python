from ArithmeticOperator import ArithmeticOperator
from AssignmentStatement import AssignmentStatement
from BinaryExpression import BinaryExpression
from BooleanExpression import BooleanExpression
from StatementSequence import StatementSequence
from Id import Id
from IfStatement import IfStatement
from LexicalAnalyzer import LexicalAnalyzer
from LiteralInteger import LiteralInteger
from ParserException import ParserException
from PrintStatement import PrintStatement
from Program import Program
from RelationalOperator import RelationalOperator
from TokenType import TokenType
from RepeatStatement import RepeatStatement
from WhileStatement import WhileStatement


class Parser():

	def __init__(self, file_name):
		print("intro")
		self.Memory = Memory()
		self.lex = LexicalAnalyzer(file_name)
		print("outro test")

	def parse(self):
		tok = self.get_next_token()
		self.match(tok, TokenType.MODULE_TOK)
		var = get_id()
		tok = self.get_next_token()
		self.match(tok, TokenType.SEMI_COLON_TOK)
		tok = self.get_next_token()
		self.match(tok, TokenType.BEGIN_TOK)
		seq = self.get_statement_seq()
		tok = self.get_next_token()
		self.match(tok, TokenType.END_TOK)
		var1 = self.get_id()
		if var.get_char() == var1.get_char():
			raise ParserException("Id must match header id")
		tok = self.get_next_token()
		self.match(tok, TokenType.PERIOD_TOK)
		tok = self.get_next_token()
		if tok.get_token_type() != TokenType.EOS_TOK:
			raise ParserException("File end error")
		return Program(seq)

	def get_statement_seq(self):
		ss = StatementSequence()
		stmt = self.get_statement()
		ss.add(stmt)
		tok = self.get_next_token()
		self.match(tok, TokenType.SEMI_COLON_TOK)
		tok = self.get_lookahead_token()
		while self.is_valid_start_of_statement(tok):
			stmt1 = self.get_statement()
			ss.add(stmt1)
			tok = self.get_next_token()
			self.match(tok, TokenType.SEMI_COLON_TOK)
			tok = self.get_lookahead_token()
		return ss

	def is_valid_start_of_statement(self, tok):
		assert tok
		return (tok.get_token_type() == TokenType.ID_TOK) or (tok.get_token_type() == TokenType.IF_TOK) or (tok.get_token_type() == TokenType.WHILE_TOK) or (tok.get_token_type() == TokenType.PRINT_TOK) or (tok.get_token_type() == TokenType.REPEAT_TOK)

	def get_statement(self):
		tok = self.get_lookahead_token()
		if tok.get_token_type() == TokenType.ID_TOK:
			stmt = self.get_assignment_statement()
		elif tok.get_token_type() == TokenType.IF_TOK:
			stmt = self.get_if_statement()
		elif tok.get_token_type() == TokenType.PRINT_TOK:
			stmt = self.get_print_statement()
		elif tok.get_token_type() == TokenType.REPEAT_TOK:
			stmt = self.get_repeat_statement()
		elif tok.get_token_type() == TokenType.WHILE_TOK:
			stmt = self.get_while_statement()
		else:
			raise ParserException("Statement expected")
		return stmt

	def get_while_statement(self):
		tok = self.get_next_token()
		self.match(tok, TokenType.WHILE_TOK)
		expr = self.get_boolean_expression()
		tok = self.get_next_token()
		self.match(tok, TokenType.DO_TOK)
		ss = self.get_statement_seq()
		tok = self.get_next_token()
		self.match(tok, TokenType.END_TOK)
		return WhileStatement(expr, ss)

	def get_repeat_statement(self):
		tok = self.get_next_token()
		self.match(tok, TokenType.WHILE_TOK)
		expr = self.get_boolean_expression()
		tok = self.get_next_token()
		self.match(tok, TokenType.DO_TOK)
		ss = self.get_statement_seq()
		tok = self.get_next_token()
		self.match(tok, TokenType.END_TOK)
		return RepeatStatement(expr, ss)

	def get_if_statement(self):
		tok = self.get_next_token()
		self.match(tok, TokenType.IF_TOK)
		expr = self.get_boolean_expression()
		tok = self.get_next_token()
		self.match(tok, TokenType.THEN_TOK)
		ss1 = self.get_statement_seq()
		tok = self.get_next_token()
		self.match(tok, TokenType.ELSE_TOK)
		ss2 = self.get_statement_seq()
		tok = self.get_next_token()
		self.match(tok, TokenType.END_TOK)
		return IfStatement(expr, ss1, ss2)

	def get_print_statement(self):
		tok = self.get_next_token()
		self.match(tok, TokenType.PRINT_TOK)
		tok = self.get_next_token()
		self.match(tok, TokenType.LEFT_PAREN_TOK)
		expr = self.get_expression()
		tok = self.get_next_token()
		self.match(tok, TokenType.RIGHT_PAREN_TOK)
		expr = self.get_expression()
		return PrintStatement(expr)

	def get_assignment_statement(self):
		var = self.get_id()
		tok = self.get_next_token()
		self.match(tok, TokenType.ASSIGN_OP)
		expr = self.get_expression()
		return AssignmentStatement(var, expr)

	def get_expression(self):
		tok = self.get_lookahead_token()
		if tok.get_token_type() == TokenType.ID_TOK:
			expr = self.get_id()
		elif tok.get_token_type() == TokenType.LIT_INT:
			tok = self.get_next_token()
			try:
				expr = LiteralInteger(int(tok.get_lexeme()))
			except ParserException("Integer constant expected") as e:
				print(e)
		else:
			op = self.get_arithmetic_operator()
			expr1 = self.get_expression()
			expr2 = self.get_expression()
			expr = BinaryExpression(op, expr1, expr2)
		return expr

	def get_arithmetic_operator(self):
		tok = self.get_next_token()
		if tok.get_token_type() == TokenType.ADD_TOK:
			op = ArithmeticOperator.ADD_OP
		elif tok.get_token_type() == TokenType.SUB_TOK:
			op = ArithmeticOperator.SUB_OP
		elif tok.get_token_type() == TokenType.MUL_TOK:
			op = ArithmeticOperator.MUL_OP
		elif tok.get_token_type() == TokenType.DIV_TOK:
			op = ArithmeticOperator.DIV_OP
		else:
			raise ParserException("Arithmetic Operator expected")
		return op

	def get_boolean_expression(self):
		op = self.get_relational_operator()
		expr1 = self.get_expression()
		expr2 = self.get_expression()
		return BooleanExpression(op, expr1, expr2)

	def get_relational_operator(self):
		tok = self.get_next_token()
		if tok.get_token_type() == TokenType.NE_TOK:
			op = RelationalOperator.NE_OP
		elif tok.get_token_type() == TokenType.EQ_TOK:
			op = RelationalOperator.EQ_OP
		elif tok.get_token_type() == TokenType.LT_TOK:
			op = RelationalOperator.LT_OP
		elif tok.get_token_type() == TokenType.LE_TOK:
			op = RelationalOperator.LE_OP
		elif tok.get_token_type() == TokenType.GT_TOK:
			op = RelationalOperator.GT_OP
		elif tok.get_token_type() == TokenType.GE_TOK:
			op = RelationalOperator.GE_OP
		else:
			raise ParserException("Relational operator expected")
		return op
		
	def get_id(self):
		tok = self.get_next_token()
		self.match(tok, TokenType.ID_TOK)
		return Id(tok.get_lexeme()[0])
	
	#litintworkaround
	
	def match(self, tok, tokType):
		if tok.get_token_type() != tokType:
			raise ParserException(tokType + " expected")

	def get_next_token(self):
		try:
			tok = self.lex.get_next_token()
		except ParserException("No next token") as e:
			print(e)
		return tok

	def get_lookahead_token(self):
		try:
			tok = self.lex.get_lookahead_token()
		except ParserException("No lookahead token") as e:
			print(e)
		return tok
