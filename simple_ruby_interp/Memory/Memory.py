#


class Memory():
    mem = []
    for x in range(52):
        mem.append(0)

    def fetch(self, var):
        assert var
        return self.mem[self.get_index(var.get_char())]

    def store(self, var, value):
        assert var
        assert value
        self.mem[self.get_index(var.get_char())] = value

    def get_index(self, ch):
        assert ch
        if ch.isupper():
            index = ch - 'A'
        else:
            index = ch + '26'
        return index