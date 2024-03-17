
document.getElementById("next").addEventListener("click", function () {

    var itemID= getElementById("item").innerText;
    itemID*=1;
    itemID+=1;
    getElementById("item").innerText=itemID;
  
});
document.getElementById("back").addEventListener("click", function () {

    var itemID= getElementById("item").innerText;
    itemID*=1;
    itemID-=1;
    getElementById("item").innerText=itemID;
  
});

/*
document.getElementById("next").addEventListener("click", function () {
    alert("next");
    // Add more functionality here (e.g., update pet's health)
  });
  
  document.getElementById("back").addEventListener("click", function () {
    alert("back");
    // Add more functionality here (e.g., update pet's happiness)
  });
  */

  

