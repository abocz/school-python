#
from ArithmeticOperator import ArithmeticOperator
from AssignmentStatement import AssignmentStatement
from BinaryExpression import BinaryExpression
from BooleanExpression import BooleanExpression
from CodeBlock import CodeBlock
from Expression import Expression
from Id import Id
from IfStatement import IfStatement
from LexicalAnalyzer import LexicalAnalyzer
from LiteralInterger import LiteralInteger
from ParserException import ParserException
from PrintStatement import PrintStatement
from Program import Program
from RelationalOperator import RelationalOperator
from TokenType import TokenType
from UntilStatement import UntilStatement
from WhileStatement import WhileStatement


class Parser():

    def __init__(self, file_name):
        assert file_name
        self.lex = LexicalAnalyzer(file_name)

    def parse(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.DEF_TOK)
        cb = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.END_TOK)
        tok = self.get_next_token()
        if tok.get_token_type() != TokenType.EOS_TOK:
            raise ParserException("Garbage at end of program")
        return Program(cb)

    def get_codeblock(self):
        cd = CodeBlock()
        stmt = self.get_statement()
        cd.add(stmt)
        tok = self.get_lookahead_token()
        while self.is_valid_start_of_statement(tok):
            stmt = self.get_statement()
            cd.add(stmt)
            tok = self.get_lookahead_token()
        return cd

    def is_valid_start_of_statement(self, tok):
        assert tok
        return (tok.getTokenType() == TokenType.ID_TOK) or (tok.getTokenType() == TokenType.IF_TOK) or (tok.getTokenType() == TokenType.WHILE_TOK) or (tok.getTokenType() == TokenType.UNTIL_TOK) or (tok.getTokenType() == TokenType.PUTS_TOK)

    def get_statement(self):
        tok = self.get_lookahead_token()
        if tok.get_token_type() == TokenType.ID_TOK:
            stmt = self.get_assignment_statement()
        elif tok.get_token_type() == TokenType.IF_TOK:
            stmt = self.get_if_statement()
        elif tok.get_token_type() == TokenType.PUTS_TOK:
            stmt = self.get_print_statement()
        elif tok.get_token_type() == TokenType.UNTIL_TOK:
            stmt = self.get_until_statement()
        elif tok.get_token_type() == TokenType.WHILE_TOK:
            stmt = self.get_while_statement()
        else:
            raise ParserException("Statement expected", tok.get_row_number(), tok.get_column_number)
        return stmt

    def get_while_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.WHILE_TOK)
        expr = self.get_boolean_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.DO_TOK)
        cb = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.END_TOK)
        return WhileStatement(expr, cb)

    def get_until_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.WHILE_TOK)
        expr = self.get_boolean_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.DO_TOK)
        cb = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.END_TOK)
        return UntilStatement(expr, cb)

    def get_if_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.IF_TOK)
        expr = self.get_boolean_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.THEN_TOK)
        cb1 = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.ELSE_TOK)
        cb2 = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.END_TOK)
        return IfStatement(expr, cb1, cb2)

    def get_print_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.PUTS_TOK)
        expr = self.get_expression()
        return PrintStatement(expr)

    def get_assignment_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.ID_TOK)
        var = Id(tok.get_lexeme()[0])
        tok = self.get_next_token()
        self.match(tok, TokenType.ASSIGN_OP)
        expr = self.get_expression()
        return AssignmentStatement(var, expr)

    def get_expression(self):
        expr = Expression()
        tok = self.get_lookahead_token()
        if tok.get_token_type() == TokenType.ID_TOK:
            tok = self.get_next_token()
            expr = Id(tok.get_lexeme()[0])
        elif tok.get_token_type() == TokenType.LIT_INT:
            tok = self.get_next_token()
            try:
                expr = LiteralInteger(int(tok.get_lexeme()))
            except ParserException("Integer constant expected", tok.get_row_number(), tok.get_column_number()) as e:
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
            raise ParserException("Arithmetic Operator expected", tok.get_row_number, tok.get_column_number)
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
            raise ParserException("Relational operator expected at ", tok.get_row_number(), tok.get_column_number())
        return op

    def match(self, tok, tokType):
        assert tok
        assert tokType
        if tok.get_token_type() != type:
            raise ParserException(type + " expected at ", tok.get_line_number(), tok.get_column_number())

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