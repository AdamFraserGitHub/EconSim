class Buisness:
    def __init__(self, seedCapital, birthItteration, oppExpend, ID):
        self.capital = seedCapital # the capital the buisness started with
        self.birthItteration = birthItteration # the global itteration the buisness was created on (like a date)
        self.itterations = 0 # the number of itterations the buisness has survived 
        self.oppExpend = oppExpend # background opperational expendetures as a fraction of capital

        self.goodsHeld = [] # the goods this buisness has a hold of i.e. goods it does and can continue to produce

        self.freeCapital = 0 # ok this needs ... work

    def addGoods(good, quantity):
        #search currently held goods and if the good to be added is
        #already produced simply add to the quantity of that good produced
        goodAlreadyProduced = False
        for goodHeld in goodsHeld:
            if goodHeld["data"] == good:
                goodHeld["quantity"] += quantity
                goodAlreadyProduced = True
                break

        # if the good to be add is not already produced by this buisness then
        # add a new entry for that good with the corresponding quantity
        if not goodAlreadyProduced:
            goodsHeld.append({
                "data": good,
                "quantity": quantity
            })



    def itterate():
        totalTurnRevenue = 0
        totalTurnCosts = 0

        #calculate revenue (costs + profit) and costs
        for goodHeld in goodsHeld:
            totalTurnRevenue += goodHeld["data"].absProfit * goodHeld["quantity"]
            totalTurnCosts += goodHeld["data"].absCost * goodHeld["quantity"]

        # the following is a bit odd and inefficeint but it has more grounding in reality
        # where costs come from capital and are returned with interest in revenue. in future 
        # additions this may be usefull to demonstrate what happens when a company overestimates
        # demand
        capital -= capital*oppExpend
        capital -= totalTurnCosts
        capital += totalTurnRevenue

        itterations += 1
