const plants = [
    '/static/images/plant1.png',
    '/static/images/plant2.png',
    '/static/images/plant3.png',
    '/static/images/plant4.png',
    ];
var currentIndex = 1;
var leaves = 0;
    
document.getElementById("bin-button").addEventListener("click",function (){
    
    console.log("Current index:", currentIndex, " pl: ", plants.length);
    if (currentIndex === plants.length){
        currentIndex = 0;
        leaves +=5;
        document.getElementById("leavesCounter").innerText = leaves;
    }

    document.getElementById("plant-image").src = plants[currentIndex];
    currentIndex = currentIndex + 1;
    console.log("end");
});

document.getElementById("feed-button").addEventListener("click", function () {
    alert("Yum! Thanks for feeding me.");
  });
  
  document.getElementById("play-button").addEventListener("click", function () {
    alert("Yay! Playing is fun.");
  });

document.addEventListener("DOMContentLoaded", function () {
    applySavedItems(); // Apply the saved items to the pet on the home page
  });
  
  function applySavedItems() {
    const items = [
      "/static/images/socks.png",
      "/static/images/bottle.png",
      "/static/images/crown.png",
      "/static/images/cap.png",
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