from AssignmentStatement import AssignmentStatement
from BinaryExpression import BinaryExpression
from BooleanExpression import BooleanExpression
from ConstantExpression import ConstantExpression
from DoStatement import DoStatement
from IfStatement import IfStatement
from LexicalAnalyzer import LexicalAnalyzer
from ParserException import ParserException
from PrintStatement import PrintStatement
from Program import Program
from StatementList import StatementList
from TokenType import TokenType
from VariableExpression import VariableExpression


class Parser():
	def __init__(self, fileName):
		if not fileName:
			raise ValueError("null file name")
		self.lex = LexicalAnalyzer(fileName)
	def parse(self):
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.PROGRAM_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.ID_TOK)
		id = tok.getLexeme()
		sList = StatementList(self.getStatementList())
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.END_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.PROGRAM_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.ID_TOK)
		if id == tok.getLexeme():
			raise ParserException("invalid id", tok.getRowNum(), tok.getColumnNum())
		proggy = Program(sList)
		return proggy
	def getStatementList(self):
		sList = StatementList()
		s = self.getStatement()
		sList.add(s)
		tok = self.lex.getLookaheadToken()
		while self.isValidStartOfStatement(tok):
			s = self.getStatement()
			sList.add(s)
			tok = self.lex.getLookaheadToken()
		return sList
	def isValidStartOfStatement(self, tok):
		assert tok is not None
		if tok.getTokenType() == TokenType.ID_TOK or tok.getTokenType() == TokenType.DO_TOK or tok.getTokenType() == TokenType.IF_TOK or tok.getTokenType() == TokenType.WRITE_TOK:
			return True
		else:
			return False
	def getStatement(self):
		tok = self.lex.getLookaheadToken()
		if tok.getTokenType() == TokenType.IF_TOK:
			s = self.getIfStatement()
		elif tok.getTokenType() == TokenType.ID_TOK:
			s = self.getAssignmentStatement()
		elif tok.getTokenType() == TokenType.DO_TOK:
			s = self.getDoStatement()
		elif tok.getTokenType() == TokenType.WRITE_TOK:
			s = self.getPrintStatement()
		else:
			raise ParserException("statement expected", tok.getRowNum(), tok.getColumnNum())
		return s
	def getPrintStatement(self):
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.WRITE_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.LEFT_PAREN_TOK)
		expr = self.getExpression()
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.RIGHT_PAREN_TOK)
		pState = PrintStatement(expr)
		return pState
	def getDoStatement(self):
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.DO_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.ID_TOK)
		#maybe issues here
		ch = tok.getLexeme()[0]
		var = VariableExpression(ch)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.ASSSIGNMENT_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.INT_TOK)
		first = int(tok.getLexeme())
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.COMMA_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.INT_TOK)
		last = int(tok.getLexeme())
		sList = StatementList(self.getStatementList())
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.END_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.DO_TOK)
		doer = DoStatement(var, first, last, sList)
		return doer
	def getAssignmentStatement(self):
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.DO_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.ID_TOK)
		#maybe same issue
		ch = tok.getLexeme()[0]
		var = VariableExpression(ch)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.ASSIGNMENT_TOK)
		expr = self.getExpression()
		assState = AssignmentStatement(var,expr)
		return assState
	def getIfStatement(self):
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.IF_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.LEFT_PAREN_TOK)
		expr = self.getBooleanExpression()
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.RIGHT_PAREN_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.THEN_TOK)
		sList1 = StatementList(self.getStatementList())
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.ELSE_TOK)
		sList2 = StatementList(self.getStatementList())
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.END_TOK)
		tok = self.lex.getNextToken()
		self.match(tok, TokenType.IF_TOK)
		iffer = IfStatement(expr, sList1, sList2)
		return iffer
	def getBooleanExpression(self):
		#maybe issue here due to correct object type
		#also consolidate with below function to perhap fix
		op = self.getRelativeOperator()
		expr1 = self.getExpression()
		expr2 = self.getExpression()
		boo = BooleanExpression(op, expr1, expr2)
		return boo
	#maybe issue, with relative operator enum situation	
	def getRelativeOperator(self):
		tok = self.lex.getNextToken()
		if tok.getTokenType() == TokenType.LT_TOK:
			op = BooleanExpression.RelativeOperator.LT
		elif tok.getTokenType() == TokenType.LE_TOK:
			op = BooleanExpression.RelativeOperator.LE
		elif tok.getTokenType() == TokenType.GT_TOK:
			op = BooleanExpression.RelativeOperator.GT
		elif tok.getTokenType() == TokenType.GE_TOK:
			op = BooleanExpression.RelativeOperator.GE
		elif tok.getTokenType() == TokenType.EQ_TOK:
			op = BooleanExpression.RelativeOperator.EQ
		elif tok.getTokenType() == TokenType.NE_TOK:
			op = BooleanExpression.RelativeOperator.NE
		else:
			raise ParserException("relational operator expected", tok.getRowNum(), tok.getColumnNum())
		return op
	def getExpression(self):
		tok = self.lex.getNextToken()
		if tok.getTokenType() == TokenType.ID_TOK:
			tok = self.lex.getNextToken()
			expr = VariableExpression(tok.getLexeme()[0])
		elif tok.getTokenType() == TokenType.INT_TOK:
			tok = self.lex.getNextToken()
			expr = ConstantExpression(int(tok.getLexeme()))
		else:
			op = self.getArithmeticOperator()
			expr1 = self.getExpression()
			expr2 = self.getExpression()
			expr = BinaryExpression(op, expr1, expr2)
	def getArithmeticOperator(self):
		tok = self.lex.getNextToken()
		if tok.getTokenType() == TokenType.ADD_TOK:
			op = BinaryExpression.ArithmeticOperator.ADD_OP
		elif tok.getTokenType() == TokenType.SUB_OP:
			op = BinaryExpression.ArithmeticOperator.SUB_OP
		elif tok.getTokenType() == TokenType.MUL_OP:
			op = BinaryExpression.ArithmeticOperator.MUL_OP
		elif tok.getTokenType() == TokenType.DIV_OP:
			op = BinaryExpression.ArithmeticOperator.DIV_OP
		else:
			raise ParserException("arithmetic op error", tok.getRowNum(), tok.getColumnNum())
		return op
	def match(self, tok, expected):
		assert tok is not None
		if tok.getTokenType() != expected:
			# ParserException(doesn't print expected token)
			raise ParserException(expected + " expected", tok.getRowNum(), tok.getColumnNum())