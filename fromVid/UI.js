var numSellersLabel = document.getElementById('numSellersLabel');
var numBuyersLabel = document.getElementById('numBuyersLabel');

var sellersSlider = document.getElementById('sellersSlider');
var buyersSlider = document.getElementById('buyersSlider')

function updateNumSellers() {
    numSellersLabel.innerHTML = "number of sellers: " + sellersSlider.value;
}

function updateNumBuyers() {
    numBuyersLabel.innerHTML = "number of buyers: " + buyersSlider.value;
}