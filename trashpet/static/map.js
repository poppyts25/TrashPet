var map = L.map('map').setView([50.7374, -3.5351], 13); // Centered at University of Exeter

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // University of Exeter Marker (Green)
        var exeterMarker = L.marker([50.7374, -3.5351], {
            icon: L.icon({
                iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
                iconSize: [38, 95],
                iconAnchor: [22, 94],
                popupAnchor: [-3, -76]
            })
        }).addTo(map);

        exeterMarker.bindPopup("<b>University of Exeter</b>").openPopup();

        // Get User's Location
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var userLocation = L.marker([position.coords.latitude, position.coords.longitude], {
                    icon: L.icon({
                        iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-red.png',
                        iconSize: [38, 95],
                        iconAnchor: [22, 94],
                        popupAnchor: [-3, -76]
                    })
                }).addTo(map);

                userLocation.bindPopup("<b>Your Location</b>").openPopup();
            }, function() {
                alert('Error: The Geolocation service failed.');
            });
        } else {
            alert('Error: Your browser doesn\'t support geolocation.');
        }