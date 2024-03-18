var myZoom = 13;

var map = L.map('map').setView([50.7374, -3.5351], 13); // Centered at University of Exeter

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var uniicon = L.icon({
    iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
    iconSize: [19, 47],
    iconAnchor: [11, 47],
    popupAnchor: [-3, -38]
});

// University of Exeter Marker (Green)
var exeterMarker = L.marker([50.7374, -3.5351], {
    icon: uniicon
}).addTo(map);
exeterMarker.bindPopup("<b>University of Exeter</b>");
var lukesMarker = L.marker([50.7374, -3.5351], {
    icon: uniicon
}).addTo(map);
lukesMarker.bindPopup("<b>University of Exeter</b>");
var penrynMarker = L.marker([50.7374, -3.5351], {
    icon: uniicon
}).addTo(map);
penrynMarker.bindPopup("<b>University of Exeter</b>");

// Marker for user location
var userLocation = L.marker([50.737, -3.535], {
    icon: L.icon({
        iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-red.png',
        iconSize: [19, 47],
        iconAnchor: [11, 47],
        popupAnchor: [-3, -38]
    })
}).addTo(map);
userLocation.bindPopup("<b>Your Location</b>").openPopup();


// Function to calculate distance between two points using Haversine formula
function calculateDistance(lat1, lon1, lat2, lon2) {
    const R = 6371.0; // Earth radius in kilometers

    const radians = function(degrees) {
        return degrees * Math.PI / 180;
    };

    const dLat = radians(lat2 - lat1);
    const dLon = radians(lon2 - lon1);
    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(radians(lat1)) * Math.cos(radians(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    const distance = R * c;
    return distance;
}

// Function to update user's location marker
function updateUserLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            userLocation.setLatLng([position.coords.latitude, position.coords.longitude]);
        }, function() {
            alert('Error: Failed to get a location');
            userLocation.bindPopup("<b>Default location</b>");
            userLocation.setLatLng([50.737, -3.535]);
        });
    } else {
        alert('Error: Your browser doesn\'t support geolocation.');
        userLocation.bindPopup("<b>Default location</b>");
        userLocation.setLatLng([50.737, -3.535]);
    }
}


//initial function call
updateUserLocation();
// Call updateUserLocation() every 10 seconds
setInterval(updateUserLocation, 10000);

var initialLat;
var initialLang;
function timer() {
    var seconds=document.getElementById("seconds");
    var updatedSeconds= seconds.innerText;
			updatedSeconds*=1;
			updatedSeconds+=1;
			
   
    if (updatedSeconds==60) {
        var mins=document.getElementById("mins");
        var updatedMins= mins.innerText;
		updatedMins*=1;
		updatedMins+=1;
		mins.innerText=updatedMins;
        updatedSeconds=0;
    }
    
    seconds.innerText=updatedSeconds;

}
var intervalId
document.getElementById("start-stop").addEventListener("click", function () {
    var startStop = document.getElementById("start-stop");
    if (startStop.innerText=="Start Walking") {
        startStop.innerText="Stop Walking";//chnage button text
        var initialLatLng = userLocation.getLatLng();
        initialLat = initialLatLng.lat;
        initialLang = initialLatLng.lng;

        //start timer 
        document.getElementById("Time").innerHTML="You have been walking for <a id='mins'>0</a>minutes and <a id='seconds'>0</a> seconds";
        intervalId = setInterval(timer,1000);
     
    } else {
        startStop.innerText="Start Walking";//change button text
        var finalLatLang = userLocation.getLatLng();
        finalLat = finalLatLang.lat;
        finalLang = finalLatLang.lng;
        var distance=calculateDistance(initialLat,initialLang,finalLat,finalLang)
        clearInterval(intervalId);
        document.getElementById("Distance").innerText = "Distance travelled: " + distance.toFixed(2) + " km";

    }
  });
