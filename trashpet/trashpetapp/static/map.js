var myZoom=13;

var map = L.map('map').setView([50.7374, -3.5351], 13); // Centered at University of Exeter

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
        var  uniicon= L.icon({
          iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
          iconSize: [19, 47], 
          iconAnchor: [11, 47], 
          popupAnchor: [-3, -38] 
      })
        // University of Exeter Marker (Green)
        var exeterMarker = L.marker([50.7374, -3.5351], {icon:uniicon}).addTo(map);
        exeterMarker.bindPopup("<b>University of Exeter</b>").openPopup();
        var penrynMarker = L.marker([50.1710, -5.1238], {icon:uniicon}).addTo(map);
        penrynMarker.bindPopup("<b>University of Exeter</b>").openPopup();
        var lukesMarker = L.marker([50.7224, -3.5166], {icon:uniicon}).addTo(map);
        lukesMarker.bindPopup("<b>University of Exeter</b>").openPopup();

        
      
        //initial set up of user location
        var userLocation = L.marker([50.737, -3.535], {
          icon: L.icon({
              iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-red.png',
              iconSize: [38, 95],
              iconAnchor: [22, 94],
              popupAnchor: [-3, -76]
          })
      }).addTo(map);

      
          if (navigator.geolocation) {
              navigator.geolocation.getCurrentPosition(function(position) {
                  userLocation.bindPopup("<b>Your Location</b>").openPopup();
                  userLocation.setLatLng([position.coords.latitude, position.coords.longitude]);
                  map.setView([position.coords.latitude, position.coords.longitude], myZoom);
              }, function() {
                  alert('Error: The Geolocation service failed.');
                  userLocation.bindPopup("<b>Default location</b>").openPopup();
                  map.setView([50.737, -3.535], myZoom);
              });
          } else {
              alert('Error: Your browser doesn\'t support geolocation.');
              userLocation.bindPopup("<b>Default location</b>").openPopup();
              map.setView([50.737, -3.535], myZoom);
          }
        function updateUserLocation(){
          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                userLocation.bindPopup("<b>Your Location</b>");
                userLocation.setLatLng([position.coords.latitude, position.coords.longitude]);
             
            }, function() {
                alert('Error: The Geolocation service failed.');
                userLocation.bindPopup("<b>Default location</b>");
                userLocation.setLatLng([50.737, -3.535]);
        
            });
        } else {
            //alert('Error: Your browser doesn\'t support geolocation.');
            userLocation.bindPopup("<b>Default location</b>");
            userLocation.setLatLng([50.737, -3.535]);
        }

        }
        

      updateUserLocation();//initial function call
      // Call updateUserLocation() every 10 seconds
      setInterval(updateUserLocation, 10000);