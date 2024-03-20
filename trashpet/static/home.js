document.getElementById("feed-button").addEventListener("click", function () {
  startEating();
});

document.getElementById("play-button").addEventListener("click", function () {
  // remove first ball if present
  let existingBall = document.getElementById("ball");
  if (existingBall) {
    existingBall.remove();
  }

  // create and add new ball image element
  let ball = document.createElement("img");
  const ballPath = "/static/images/ball.png";
  ball.id = "ball";
  ball.src = ballPath;
  ball.className = "ball";
  document.getElementById("pet-container").appendChild(ball); // add ball to pet container

  // bounce logic
  // bounce logic variables
  let bounceHeight = 0; // Start from the bottom
  let position = 0; // Initial position at the bottom
  let velocity = 10; // Initial velocity should be positive to move up
  let acceleration = -0.5; // Gravity effect should be negative to pull the ball down
  let lastTime = null;

  function animate(time) {
    if (lastTime != null) {
      velocity += acceleration; // Apply gravity
      position += velocity; // Update position based on velocity

      // Check for bounce
      if (position <= bounceHeight) {
        // Now checking if it hits the bottom
        position = bounceHeight; // Keep the ball above the floor
        velocity *= -0.7; // Reverse direction and simulate bounce
      }

      ball.style.bottom = position + "px"; // move the ball
    }
    lastTime = time;
    if (position >= bounceHeight || velocity > 0) {
      // continue if not finished
      requestAnimationFrame(animate);
    }
  }
  // start the animation
  requestAnimationFrame(animate);

  // finish after 2 seconds
  setTimeout(function () {
    ball.remove();
  }, 2000);
});

document.addEventListener("DOMContentLoaded", function () {
  applySavedItems(); // Apply the saved items to the pet on the home page
});

function startEating() {
  const petMouth = document.getElementById("mouth");
  const openMouth = "/static/images/openmouth1.png"; // Path to the open mouth image
  const smile = "/static/images/smile.png";

  petMouth.src = openMouth;

  const petContainer = document.getElementById("pet-container"); // adding to pet container
  const eatingStages = [
    "/static/images/trash.png",
    "/static/images/trash-1.png",
    "/static/images/trash-2.png",
  ];

  let index = 0;
  const eatingAnimation = document.createElement("img"); // adding to dom
  eatingAnimation.src = eatingStages[index]; // set up source
  eatingAnimation.id = "eating-animation";
  eatingAnimation.className = "pet-layered-item";
  petContainer.appendChild(eatingAnimation);

  function eat() {
    petMouth.src = openMouth;
    setTimeout(() => {
      petMouth.src = smile; // Change back to the smile
    }, 200);
    index += 1; // increment by one
    if (index < eatingStages.length) {
      // cycle through images
      eatingAnimation.src = eatingStages[index];
      setTimeout(eat, 800); // 800ms gap between images
    } else {
      eatingAnimation.remove();
    }
  }
  setTimeout(eat, 400); //400ms delay before first 'bite' taken
}

function applySavedItems() {
  items.forEach((item, index) => {
    const itemId = `item-${index}`;
    if (!document.getElementById(itemId)) {
      // Check to avoid duplicating the item
      const newItem = document.createElement("img");
      newItem.src = item;
      newItem.className = "pet-layered-item";
      newItem.id = itemId;
      document.getElementById("pet-container").appendChild(newItem);
    }

  });

  const savedBackgroundImage = pet_colour;
  if (savedBackgroundImage) {
    document.querySelector(".pet-background").src = savedBackgroundImage;
  }
}
