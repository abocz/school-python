from enum import Enum


class RelationalOperator(Enum):
	EQ_OP, NE_OP, LT_OP, LE_OP, GT_OP, GE_OP = range(6)