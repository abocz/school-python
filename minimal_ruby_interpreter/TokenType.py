#Finished
from enum import Enum


class TokenType(Enum):
    """
    Enum Class for TokenType
    23 different types
    """
    DEF_TOK, END_TOK, IF_TOK, PUTS_TOK, UNTIL_TOK, ID_TOK, WHILE_TOK, ELSE_TOK, THEN_TOK, ASSIGN_OP, LIT_INT, ADD_TOK, SUB_TOK, MUL_TOK, DIV_TOK, EQ_TOK, NE_TOK, LT_TOK, LE_TOK, GT_TOK, GE_TOK, EOS_TOK, DO_TOK = range(23)
