//list of paths to images
const plants = [
    '/static/images/plant1.png',
    '/static/images/plant2.png',
    '/static/images/plant3.png',
    '/static/images/plant4.png',
    ];
//set current index to 1 as image 1 is the default
var currentIndex = 1;
   
//run when bin button is clicked
document.getElementById("bin-button").addEventListener("click",function (){
    //reset back to start of list if variable is too long
    if (currentIndex === plants.length){
        currentIndex = 0;
    }

    //change plant image src to the next image to show
    document.getElementById("plant-image").src = plants[currentIndex];

    //increment index
    currentIndex = currentIndex + 1;
});

//alert placeholder for feed button
document.getElementById("feed-button").addEventListener("click", function () {
    alert("Yum! Thanks for feeding me.");
});
  
//alert placeholder for play buttin
document.getElementById("play-button").addEventListener("click", function () {
    alert("Yay! Playing is fun.");
});

//when page loads, run applySavedItems function
document.addEventListener("DOMContentLoaded", function () {
    applySavedItems();
});
  

function applySavedItems() {

  const items = home.attr('data-items')
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