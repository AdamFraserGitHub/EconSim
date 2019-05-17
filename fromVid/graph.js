var avgPriceGraph = document.getElementById('avgGoodPriceGraph');
var avgPriceCanvas = avgPriceGraph.getContext('2d')
var avgPriceCanvasW = avgPriceGraph.width = Math.floor(window.innerWidth * 0.6);
var avgPriceCanvasH = avgPriceGraph.height = Math.floor(window.innerHeight * 0.6);

avgPriceCanvas.translate(0.5,0.5) //prevents blurriness in lines (just how the API works)

var graphPoints = [];

class GraphPoint {
    constructor(xDraw, yDraw, price) {
        this.xDraw = xDraw;
        this.yDraw = yDraw;
        this.price = price;
    }
}

function renderGraph() {
    //draw graph axes
    avgPriceCanvas.strokeStyle = 'rgb(0,0,0)'
    avgPriceCanvas.beginPath();
        avgPriceCanvas.moveTo(5,5);
        avgPriceCanvas.lineTo(5, avgPriceCanvasH - 5);
        avgPriceCanvas.lineTo(avgPriceCanvasW - 5, avgPriceCanvasH - 5);
        avgPriceCanvas.stroke();
    avgPriceCanvas.closePath();

    avgPriceCanvas.beginPath();
        avgPriceCanvas.moveTo(graphPoints[0].xDraw, graphPoints[0].yDraw);
        for(var i = 1; i < graphPoints.length; i++) {
            avgPriceCanvas.lineTo(graphPoints[i].xDraw, graphPoints[i].yDraw);
        }
        avgPriceCanvas.stroke();
    avgPriceCanvas.closePath();
}

var t = 0;
var maxPossiblePrice = 1;
function addDataPointToGraph(priceValue) {
    var xDraw = t + 5 + 1; // the x point that the price will be drawn at to avoid drawing over anything else
    //finds the value as a fraction of the maximum possible value, maps that the the size of the graph and then 
    //flips it because of how y coordinates work in the canvas API
    var yDraw = avgPriceCanvasH - Math.round((priceValue / maxPossiblePrice) * avgPriceCanvasH) - 5 - 1;

    //add this point with its drawing data and raw data to a list of points
    graphPoints.push(new GraphPoint(xDraw, yDraw, priceValue));

    t++;
}
