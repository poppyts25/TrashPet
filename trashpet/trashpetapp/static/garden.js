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

//when page loads, run applySavedItems function
document.addEventListener("DOMContentLoaded", function () {
    applySavedItems();
});
  
function applySavedItems() {
  items.forEach((item) => {
      const newItem = document.createElement("img");
      newItem.src = item;
      newItem.className = "pet-layered-item";
      document.getElementById("pet-container").appendChild(newItem);
    
    
  });

  document.querySelector(".pet-background").src = pet_colour;
  
}