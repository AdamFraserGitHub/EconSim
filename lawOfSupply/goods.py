class Good:
    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price

        self.proffit = price - cost
        self.proffitPerc = self.proffit / cost



def defaultGoods():
    goodsReturn = []