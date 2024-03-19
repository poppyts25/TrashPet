document.getElementById("feed-button").addEventListener("click", function () {
  startEating();
});

document.getElementById("play-button").addEventListener("click", function () {
  alert("Yay! Playing is fun.");
});

document.addEventListener("DOMContentLoaded", function () {
  applySavedItems(); // Apply the saved items to the pet on the home page
});

function startEating() {
  const petContainer = document.getElementById("pet-container");
  const eatingStages = [
    "/static/images/trash.png",
    "/static/images/trash-1.png",
    "/static/images/trash-2.png",
  ];

  let stageIndex = 0;
  const eatingAnimation = document.createElement("img");
  eatingAnimation.src = eatingStages[stageIndex];
  eatingAnimation.id = "eating-animation";
  eatingAnimation.className = "pet-layered-item";
  petContainer.appendChild(eatingAnimation);

  function eat() {
    stageIndex += 1;
    if (stageIndex < eatingStages.length) {
      eatingAnimation.src = eatingStages[stageIndex];
      setTimeout(eat, 800);
    } else {
      eatingAnimation.remove();
    }
  }

  setTimeout(eat, 500);
}

function applySavedItems() {
  const items = [
    "/static/images/socks.png",
    "/static/images/bottle.png",
    "/static/images/crown.png",
    "/static/images/cap.png",
    "/static/images/guitar.png",
  ];
  items.forEach((itemSrc, index) => {
    const itemId = `item-${index}`;
    if (localStorage.getItem(itemId)) {
      // Item was previously added, recreate it on the pet
      if (!document.getElementById(itemId)) {
        // Check to avoid duplicating the item
        const newItem = document.createElement("img");
        newItem.src = itemSrc;
        newItem.className = "pet-layered-item";
        newItem.id = itemId;
        document.getElementById("pet-container").appendChild(newItem);
      }
    }
  });

  const savedBackgroundImage = localStorage.getItem("petBackgroundImage");
  if (savedBackgroundImage) {
    document.querySelector(".pet-background").src = savedBackgroundImage;
  }
}
