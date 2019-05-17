from good import Good

def readInSim(folderPath):
    buisData = open(folderPath + "/buis.csv")
    goodsData = open(folderPath + "/goods.csv")
    metaData = open(folderPath + "/meta.csv")

    buisData = buisData.read().split("\n")
    goodsData = goodsData.read().split("\n")
    metaData = metaData.read().split("\n")

    goodDemands = []

    #split up data by collum and ignore comments
    for i in range(len(buisData)):
        buisData[i] = buisData[i].split(",")
        if(buisData[i][0] == "#"):
            del buisData[i]
        else:
            buisData[i]=float(buisData[i][0])
    for i in range(len(goodsData)):
        goodsData[i] = goodsData[i].split(",")
        if(goodsData[i][0] == "#"):
            del goodsData[i]     
        else:
            goodsData[i][1]=float(goodsData[i][1]) #cost
            goodsData[i][2]=float(goodsData[i][2]) #price

            goodsData[i] = Good(goodsData[i][0], goodsData[i][1], goodsData[i][2])
            goodDemands.append(goodsData[i][3]) #demand

    return {
        "goodsData": goodsData,
        "goodDemands": goodDemands,
        "buisData": buisData
    }
    # for i in range(len(metaData)):
    #     metaData[i] = metaData[i].split(",")
    #     if(metaData[i][0] == "#"):
    #         del metaData[i]
            