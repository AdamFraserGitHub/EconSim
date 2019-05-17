# lawOfSupply.py
# this file contains the main driver code for the program to simulate the law of supply
# doccumentation is at https://drive.google.com/open?id=1b77MEGrwl1q5jYpe8en4g9UXRr1fb89V

from buisness import Buisness
from good import Good, findGood
import simulationParse
from random import randint

defaultSeedCapital = 100 #default amount of seed capital that each buisness starts up with
itterations = 0 #number of itterations that have been run
defaultOpperationalExpendeture = 0.01 #fraction of capital that is eaten up by opperational expendeture


simFolder = input("enter the folder that your simulation files are in (it is expected that the simulations folder is local):")

simData = simulationParse.readInSim("./simulations/simFolder")

deadBuisnesses = []
buisnesses = []

goodTypes = []      # stores a list of all the types of good that can be produces
goods = []          # stores a list of all the goods in the market (basically demand)
availableGoods = [] # stores a list of all the goods that are available to be produced
                    # i.e. demanded goods that are not being supplied

for i in range(0,len(simData.goodsData)):
    goods.append({
        "data": simData.goodsData[i],
        "demand": simData.goodDemands[i]
    })

for i in range(0,len(simData.buisData)):
    buisnesses.append(Buisness(simData.buisData[i], 0, defaultOpperationalExpendeture, randint(0,100000)))

def addNewBuisness():
    buisnesses.append(Buisness(seedCapital=defaultSeedCapital, birthItteration=itterations, oppExpend=0.01, ID=randint(0,100000)))
    pass

#this is probably the most complex and least realistic funcion in the model
#it works in rounds and order by profit. first the most profitable good (in %) is 
#equally distributed amoung all buisnesses, then the excess from smaller buisnesses
#i.e. production in excess of capital is removed from those buisnesses and put back
#into the pool of demand while those same buisnesses that could not produce their 
#equal share are removed from competing for this goods production while retaining
#their production quota. this is continued. if there is 1 good left over at the end
#the buisness that gets it is decided at random. for a good that has very low demand
#it may even just be distributed equally within one round
def allocateProduction():
    #for each available good type preform the "auction" algorithm
    for availableGood in availableGoods:
        demand = availableGood["demand"]

        lockedInBuisnesses = []     #buisnesses whose production has been locked in and are n0o longer competing
        competingBuisnesses = []    #buisnesses that are still competing and that are still able to produce
        nextRoundDemandCarryOver = 0

        for i in range(0,len(buisnesses)):
            competingBuisnesses.append({
                    "data": buisnesses[i], 
                    "capacityLeft": int(buisnesses[i].freeCapital / availableGood["data"].cost), #capacity to produce the current good
                    "productionQuota": 0
                })

        while(demand > 0):
            #a single round
            #1. demand per buisness = remaining demand / number of buisnesses
            #2. for buisnesses that have had their capacity for this good met
            #   lock this in and remove them taking back excess capacity
            #3. place overused capacity back into remaing demand and do annother round
            #   unless overused capacity is 0 in which case move to the next good

            demandPerBuis = demand / len(competingBuisnesses) # calculate demand per buisness using current free demand
            demandPerBuis = int(demandPerBuis) # in an equal world find how much each buisness could produce

            #for each buisness that is still able to meet demand with spare capacity asign production and note any changes in
            #demand, capacity or ability to compete in the market (i.e. if the buisness has no more spare capacity remove it)
            for i in range(0,competingBuisnesses):
                if competingBuisnesses[i]['capacityLeft'] <= demandPerBuis: #if the buisness has remaining capacity less than or exactly equal
                                                                            #to it's potential maximum quota then asign this production to it, 
                                                                            #place spare "demand" back into the "demand pool" and remove the business
                                                                            #from competition for this good
                    competingBuisnesses[i]["productionQuota"] += competingBuisnesses[i]['capacityLeft']
                    nextRoundDemandCarryOver += demandPerBuis - competingBuisnesses[i]['capacityLeft']
                    lockedInBuisnesses.append(buisnesses.pop(i))
                else:
                    #if the buisness is more than capable of meeting it's demand quota then just give it the demand as a quota and
                    #reduce it's capacity (since capital has been eaten up in the process of meeting this quota)
                    competingBuisnesses[i]["capacityLeft"] -= demandPerBuis
                    competingBuisnesses[i]["productionQuota"] += demandPerBuis

            demand = nextRoundDemandCarryOver
            nextRoundDemandCarryOver = 0

            for i in range(0,len(lockedInBuisnesses)):
                for j in range(0,len(buisnesses)):
                    if buisnesses[j].ID == lockedInBuisnesses[i]["data"].ID:
                        buisnesses[j].addGoods(findGood(availableGood["data"].name), lockedInBuisnesses[i]["productionQuota"])

            for i in range(0,len(competingBuisnesses)):
                for j in range(0,len(buisnesses)):
                    if buisnesses[j].ID == competingBuisnesses[i]["data"].ID:
                        buisnesses[j].addGoods(findGood(availableGood["data"].name), competingBuisnesses[i]["productionQuota"])



#this procedure models growth of the economy by creating new buisnesses and demand
#in future it could be the point of integration for a more complete simulation especially
#demand shocks or integrating long term trends
def modelGrowth():
    pass

def itterate():
    allocateProduction()
    for i in range(len(buisnesses)):
        buisnesses[i].itterate()
    itterations += 1

# the following code block runs the program and ensures it itterates, it has a fair
# degree of user controllability, it also keeps track of the number of itterations

while True:
    print("\ncurrently on itteration " + str(itterations))
    print("enter a command for the program to continue")
    print("enter a number e.g. 22 to itterate the economy that many turns")
    print("press return / enter to itterate once")
    print("type \"l\" to leave the program")
    userCommand = input(":")

    isInteger = False
    try:
        int(userCommand)
        isInteger = True
    except:
        isInteger = False

    if(isInteger):
        for i in range(0,int(userCommand)):
            itterate()
    elif(userCommand == "l"):
        break
    else:
        itterate()