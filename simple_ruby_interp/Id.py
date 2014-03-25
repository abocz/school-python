from Memory.Memory import Memory


class Id():

    def __init__(self, ch):
        if not ch.isalpha:
            raise ValueError("Invalid Id")
        self.ch = ch
        self.testMem = Memory()

    def get_char(self):
        return self.ch

    def evaluate(self):
        Memory.fetch(self.testMem, self.ch)
