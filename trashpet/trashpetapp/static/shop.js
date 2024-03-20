document.addEventListener("DOMContentLoaded", function () {
  applySavedItems();
  loadItemStates(); // Load the states of items when the page loads

  document.querySelectorAll(".shop-item").forEach((item, index) => {
    item.addEventListener("click", function () {
      const itemId = `item-${index}`;
      if (!document.getElementById(itemId)) {
        // Item is being added
        const newItem = document.createElement("img");
        newItem.src = item.getAttribute("src");
        newItem.data = item.getAttribute("alt")
        newItem.className = "pet-layered-item";
        newItem.id = itemId;
        document.getElementById("pet-container").appendChild(newItem);
        item.style.outline = "2px solid green"; // Visual cue for selected item
      } else {
        // Item is being removed
        document.getElementById(itemId).remove();
        item.style.outline = "2px solid red"; // Visual cue for deselected item
      }
    });
  });
});

function loadItemStates() {
  document.querySelectorAll(".shop-item").forEach((item, index) => {
    var itemName = item.getAttribute("src").replace("/static/images/", "").replace(".png","");
    if (equipped_list[itemName]) {
      item.style.outline = "2px solid green"; // Visual cue for selected item
    } else {
      item.style.outline = "2px solid red"; // Visual cue for deselected item
    }
  });
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

  document.querySelector(".pet-background").src = pet_colour;
  
}


document
  .getElementById("color-menu-button")
  .addEventListener("click", function () {
    document.getElementById("color-menu").style.display = "block"; // Show color menu
    document.getElementById("shop-section").style.display = "none"; // Hide item menu
  });

document
  .getElementById("item-menu-button")
  .addEventListener("click", function () {
    document.getElementById("shop-section").style.display = "block"; // Show item menu
    document.getElementById("color-menu").style.display = "none"; // Hide color menu
  });

document.querySelectorAll(".color-option").forEach(function (option) {
  option.addEventListener("click", function () {
    const imagePath = option.getAttribute("data-path");
    console.log("background:", imagePath);
    document.querySelector(".pet-background").src = imagePath;
    pet_colour = imagePath;
  });
});

