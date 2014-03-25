#
from Statement import Statement


class AssignmentStatement(Statement):
    """
    Assignment Statement
    """
    def __init__(self, var, expr):
        if not var:
            raise ValueError("Invalid or Null Id Argument in AssignmentStatement")
        if not expr:
            raise ValueError("Invalid or Null expression argument in AssignmentStatement")
        self.var = var
        self.expr = expr

    def execute(self):
        #Memory.store(var, expr.evaluate)

