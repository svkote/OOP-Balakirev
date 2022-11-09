class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


tv1, tv2 = TV('Samsung', 30000), TV('LG', 32000)
table = Table('STOL', 10000)
laptop1, laptop2 = Notebook('Lenovo', 50000), Notebook('HP', 60000)

cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(laptop1)
cart.add(laptop2)
