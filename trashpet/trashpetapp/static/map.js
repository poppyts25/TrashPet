
// const layer = L.tileLayer(url, {
//   attribution: copy,
// });
// const map = L.map("map", {
//   layers: [layer],
  
// }).setView([51.505, -0.09], 13);

// var marker = L.marker([51.5, -0.09]).addTo(map);


// Creating map options
var mapOptions = {
  center: [17.385044, 78.486671],
  zoom: 10
}
// Creating a map object
var map = new L.map('map', mapOptions);

// Creating a Layer object
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Adding layer to the map
map.addLayer(layer);

// Creating a marker
var marker = L.marker([17.385044, 78.486671]);

// Adding marker to the map
marker.addTo(map);