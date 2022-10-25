import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


choices = [Line, Rect, Ellipse]

elements = [random.choice(choices)(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
                                   random.randint(1, 100)) for i in range(217)]
for i in elements:
    if 'Line' in str(i):
        i.sp = (0, 0)
        i.ep = (0, 0)
