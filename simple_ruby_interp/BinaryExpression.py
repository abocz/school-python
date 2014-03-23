#
from Expression import Expression


class BinaryExpression(Expression):

    def __init__(self, op, expr1, expr2):
        if not op:
            raise ValueError("Null ArithOp in Binary Expression")
        if not expr1 or expr2:
            raise ValueError("Null Expression Argument in BinaryExpression")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        #