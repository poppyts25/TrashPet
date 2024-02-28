// Initialize an object to keep track of added items
const addedItems = {};

function startBlinking() {
  const petEyes = document.getElementById("eyes");
  const openEyes = "/static/images/openeyes.png"; // Path to the open eyes image
  const closedEyes = "/static/images/closedeyes.png"; // Path to the closed eyes image

  function blink() {
    petEyes.src = closedEyes;
    setTimeout(() => {
      petEyes.src = openEyes;
      const randomDelay = Math.random() * (5000 - 2000) + 2500;
      setTimeout(blink, randomDelay);
    }, 200);
  }

  blink(); // Start the blinking process
}

document.addEventListener("DOMContentLoaded", function () {
  startBlinking();
});
