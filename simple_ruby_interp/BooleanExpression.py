#
from Expression import Expression


class BooleanExpression(Expression):

    def __init__(self, op, expr1, expr2):
        if not op:
            raise ValueError("Null operand in BooleanExpression")
        if not expr1 or expr2:
            raise ValueError("Null expression in BooleanExpression")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        result = True
        if self.op is EQ_OP:


        return result