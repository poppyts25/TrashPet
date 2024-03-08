
// const layer = L.tileLayer(url, {
//   attribution: copy,
// });
// const map = L.map("map", {
//   layers: [layer],
  
// }).setView([51.505, -0.09], 13);

// var marker = L.marker([51.5, -0.09]).addTo(map);


// Creating map options
var mapOptions = {
  center: [50.736509, -3.534422],
  zoom: 15
}
// Creating a map object
var map = new L.map('map', mapOptions);

// Creating a Layer object
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Adding layer to the map
map.addLayer(layer);

// Creating a marker
var uni = L.marker([50.7366, -3.5351]);
var lukes = L.marker([50.7224, -3.5166]);
var penryn = L.marker([50.1710, -5.1238]);

// Adding marker to the map
uni.addTo(map);
lukes.addTo(map);
penryn.addTo(map);

map
  .locate()
  .on("locationfound", (e) =>
    map.setView(e.latlng,15)
  )
  .on("locationerror", () =>
    map.setView([0, 0], 5)
  );
  
  var self = L.marker(e.latlng);
  self.addTo(map);
