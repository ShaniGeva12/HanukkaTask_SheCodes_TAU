
var candle_green = document.createElement("img");
candle_green.setAttribute("src", "imgs/candle_green.svg");
candle_green.setAttribute("height", "60");
candle_green.setAttribute("alt", "candle");

//---------------------------------------------------------------------------------------------------------------

var totalCandels = sum_the_candles();
sumDiv = document.getElementById("sum");
sumDiv.innerHTML+=totalCandels;

//---------------------------------------------------------------------------------------------------------------

var dayToPrint = 8;
let_there_be_light(dayToPrint);
var drawTitle = document.getElementById("drawTitle");
drawTitle.innerHTML+=dayToPrint;

//---------------------------------------------------------------------------------------------------------------

function sum_the_candles() {
    // we create a counter
    let sum = 0;

    // we add 8 times 1 + dayNumber (which starts from 1 and increases every time)
    for (let dayNumber = 1; dayNumber <= 8; dayNumber++) {
        sum += 1 + dayNumber;
    }
    return sum;
}

//---------------------------------------------------------------------------------------------------------------

function let_there_be_light(dayPrint) {
    document.getElementById("drawCandlesHere").appendChild(candle_green);

    for (let dayNumber = 1; dayNumber <= dayPrint; dayNumber++) {
        let candle = document.createElement("img");
        candle.setAttribute("src", "imgs/candle.svg");
        candle.setAttribute("height", "60");
        candle.setAttribute("alt", "candle");

        // for evety day passed we'll light a candle
        document.getElementById("drawCandlesHere").appendChild(candle);
    }
}