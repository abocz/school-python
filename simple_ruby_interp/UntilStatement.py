#Note: Should be working, concerned with execute method
from Statement import Statement


class UntilStatement(Statement):
    """
    UntilStatement statement object has BooleanExpression expr and CodeBlack cblock
    """
    def __init__(self, expr, cblock):
        if not expr:
            raise ValueError("Invalid or null expression argument in UntilStatement")
        if not cblock:
            raise ValueError("Invalid or null code block argument in UntilStatement")
        self.expr = expr
        self.cblock = cblock

    def execute(self):
        while not expr.evaluate():
            self.cblock.execute()

