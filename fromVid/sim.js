var maxMinSellPrice = 0.5;
var maxMaxBuyPrice = 0.6;
var sellerAdjustmentRate = 0.1;
var buyerAdjustmentRate = 0.1;

var buyers = []
var sellers = []

class Seller {
    constructor() {
        this.minPrice = Math.random() * maxMinSellPrice;
        this.sellPrice = this.minPrice + Math.random() / 10;
        this.hasSoldThisRound = false;
    }

    adjustToMarket() {
        if(!this.hasSoldThisRound) {
            this.sellPrice -= sellerAdjustmentRate * (this.sellPrice - this.minPrice);
            if(this.sellPrice < this.minPrice + 0.001) {
                this.sellPrice = this.minPrice  //prevents ever constantly decreasing sell prices that don't actually change anything
                                                //also catches any errors that would cause seller to sell bellow min sell price
            }
        } else {
            this.sellPrice += sellerAdjustmentRate * (this.sellPrice - this.minPrice) //TODO: this seems waay too easy
        }

        this.hasSoldThisRound = false;
    }
}

class Buyer {
    constructor() {
        this.maxPrice = Math.random() * maxMaxBuyPrice;
        this.buyPrice = this.maxPrice - Math.random() / 10;
        this.hasBoughtThisRound = false;
    }

    adjustToMarket() {
        if(!this.hasBoughtThisRound) {
            this.buyPrice += buyerAdjustmentRate * (this.maxPrice - this.buyPrice);
            if(this.buyPrice > this.maxPrice - 0.001) {
                this.buyPrice = this.maxPrice  //prevents ever constantly decreasing sell prices that don't actually change anything
                                                //also catches any errors that would cause seller to sell bellow min sell price
            }
        } else {
            this.buyPrice -= buyerAdjustmentRate * (this.maxPrice - this.buyPrice) //TODO: this seems waay too easy
        }

        this.hasBoughtThisRound = false;
    }
}





//this block of code works to create transactions between buyers and sellers.
//an explaination of the algorithm can be found in "transactionAlgo.txt"
function preformTransactions() {
    var remainingSellerIndicies = [];
    for(var i = 0; i < sellers.length; i++) {
        remainingSellerIndicies.push(i);
    }

    var remainingBuyerIndicies = [];
    for(var i = 0; i < buyers.length; i++) {
        remainingBuyerIndicies.push(i);
    }

    //setup transactions
    var sellersRemain = true;
    var i = 0;
    while(remainingBuyerIndicies.length > 0 && remainingSellerIndicies.length > 0 && i < 1000) {
        i++
        //attempts a transaction between a random buyer and a random seller
        //if the transaction was successfull then the buyers and sellers are removed
        //if not they remain in the list
        //also theres some inception level index shit going on
        var buyerIndexIndex = Math.floor(Math.random() * remainingBuyerIndicies.length)
        var sellerIndexIndex = Math.floor(Math.random() * remainingSellerIndicies.length)

        var currBuyer = buyers[remainingBuyerIndicies[buyerIndexIndex]]; //keeps things tidy
        var currSeller = sellers[remainingSellerIndicies[sellerIndexIndex]]
        if(currBuyer.buyPrice > currSeller.sellPrice) {
            currBuyer.hasBoughtThisRound = true;
            currSeller.hasSoldThisRound = true;

            currBuyer.adjustToMarket();
            currSeller.adjustToMarket();

            remainingBuyerIndicies.splice(buyerIndexIndex,1);
            remainingSellerIndicies.splice(sellerIndexIndex,1);
            console.log(Math.random())
        }
    }
}





// this block of code captures and stores a variety of economic metrics of the current simulation
function getAvgPrice() {
    var avgPrice = 0;
    for(var i = 0; i < sellers.length; i++) {
        avgPrice += sellers[i].sellPrice;
    }
    return avgPrice / sellers.length;
}

function runRound() {
    console.log("huh")
    preformTransactions();
    console.log(getAvgPrice());
}

for(var i = 0; i < 10; i++) {
    sellers.push(new Seller());
}

for(var i = 0; i < 10; i++) {
    buyers.push(new Buyer());
}