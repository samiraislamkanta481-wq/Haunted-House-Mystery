
const startBtn = document.getElementById("startBtn");
const startScreen = document.getElementById("startScreen");
const gameScreen = document.getElementById("gameScreen");

const timerDisplay = document.getElementById("timer");
const scoreDisplay = document.getElementById("score");
const foundDisplay = document.getElementById("foundCount");

const progressText = document.getElementById("progressText");
const progressFill = document.getElementById("progressFill");

const roomImage = document.getElementById("roomImage");
const hotspotLayer = document.getElementById("hotspotLayer");

let timeLeft = 420;
let score = 0;
let foundCount = 0;
let wrongClicks = 0;
let timerInterval;

const targets = [
    { name: "Old Key", x: 15, y: 82 },
    { name: "Candle", x: 42, y: 9 },
    { name: "Grandfather Clock", x: 94, y: 22 },
    { name: "Antique Book", x: 43, y: 75 },
    { name: "Mirror", x: 21, y: 28 },
    { name: "Old Photograph", x: 19, y: 24 },
    { name: "Wine Bottle", x: 82, y: 84 },
    { name: "Silver Spoon", x: 8, y: 90 },
    { name: "Skull", x: 29, y: 47 },
    { name: "Lantern", x: 80, y: 84 },
    { name: "Scissors", x: 58, y: 89 },
    { name: "Vase", x: 40, y: 49 },
    { name: "Rusted Bell", x: 75, y: 66 },
    { name: "Diary", x: 36, y: 77 },
    { name: "Flashlight", x: 67, y: 91 }
];

startBtn.addEventListener("click", function() {

    startScreen.style.display = "none";
    gameScreen.style.display = "block";

    createHotspots();
    startTimer();

});


function createHotspots() {

    targets.forEach((target, index) => {

        const button = document.createElement("button");

        button.className = "object-hotspot";

        button.style.left = target.x + "%";
        button.style.top = target.y + "%";

        button.dataset.index = index;

        button.title = target.name;

        button.addEventListener("click", function(event) {

            event.stopPropagation();

            findObject(index, button);

        });

        hotspotLayer.appendChild(button);

    });

}


function findObject(index, button) {

    if (targets[index].found) return;

    targets[index].found = true;

    button.remove();

    score += 10;
    foundCount++;

    scoreDisplay.textContent = score;

    foundDisplay.textContent = foundCount + "/15";

    progressText.textContent = foundCount + " / 15";

    progressFill.style.width = (foundCount / 15 * 100) + "%";

    const listItems = document.querySelectorAll(".object-list li");

    listItems[index].classList.add("found");

    if (foundCount >= 15) {

        clearInterval(timerInterval);

        alert("ROOM COMPLETED! NEXT ROOM UNLOCKED!");

    }

}


roomImage.addEventListener("click", function() {

    wrongClicks++;

    if (wrongClicks === 4) {

        timeLeft = Math.max(0, timeLeft - 10);

        wrongClicks = 0;

        if (timeLeft === 0) {

            gameOver();

        }

    }

});


function startTimer() {

    timerInterval = setInterval(function() {

        timeLeft--;

        updateTimer();

        if (timeLeft <= 0) {

            gameOver();

        }

    }, 1000);

}


function updateTimer() {

    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;

    timerDisplay.textContent =
        String(minutes).padStart(2, "0") + ":" +
        String(seconds).padStart(2, "0");

}


function gameOver() {

    clearInterval(timerInterval);

    alert("TIME'S UP! GAME OVER!");

}
