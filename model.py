import numpy as np
class Model:
    def __init__(self):
        self.storage = '2'
        self.prev = ''
        self.results = ''

    def enter_value(self, val):
        self.storage += str(val)
        print(self.storage)

    def percentage(self):
        self.storage = str(eval(self.storage) / 100)
        print(self.storage)

    def sqrt(self):
        self.storage = str(np.sqrt(eval(self.storage)))
        print(self.storage)

    def square(self):
        self.storage = str(eval(self.storage) ** 2)
        print(self.storage)

    def invert(self):
        self.storage = str(1 / eval(self.storage))
        print(self.storage)

    def CE(self):
        self.prev = ''

    def C(self):
        self.prev = ''
        self.storage = ''
        self.results = ''