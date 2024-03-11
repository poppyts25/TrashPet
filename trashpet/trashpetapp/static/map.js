var greenIcon = L.icon({
  iconUrl: 'test-icon.png',
 // shadowUrl: 'leaf-shadow.png',

  iconSize:     [38, 95], // size of the icon
  shadowSize:   [50, 64], // size of the shadow
  iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
  shadowAnchor: [4, 62],  // the same for the shadow
  popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});


// const layer = L.tileLayer(url, {
//   attribution: copy,
// });
// const map = L.map("map", {
//   layers: [layer],
  
// }).setView([51.505, -0.09], 13);

// var marker = L.marker([51.5, -0.09]).addTo(map);


// Creating map options
//in case this changes
var myZoom=15;

var mapOptions = {
  center: [50.736509, -3.534422],
  zoom: myZoom
}
// Creating a map object
var map = new L.map('map', mapOptions);

// Creating a Layer object
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Adding layer to the map
map.addLayer(layer);

// Creating a marker
var stretham = L.marker([50.7366, -3.5351]);
var lukes = L.marker([50.7224, -3.5166]);
var penryn = L.marker([50.1710, -5.1238]);

// Adding marker to the map
// stretham.addTo(map);
// lukes.addTo(map);
// penryn.addTo(map);

var uni = L.layerGroup([stretham, lukes, penryn])
uni.addTo(map);
//the plan here is to make a add/remove uni marker option

//set up persons location marker
//assume they on campus
// var person= L.marker([50.7366, -3.5351]);
// person.addTo(map);
// map
//   .locate()
//   .on("locationfound", (e)=>
//   update(e)
//   )
//   .on("locationerror", () =>
//     mapError()
//   );


// function mapError(){
//   person.setLatLng([50.7366, -3.5351]);
//   map.setView([50.7366, -3.5351], myZoom);
//   alert("Hello! I am an alert box!!");
// }
  

// function update(e){
//     person.setLatLng(e);
//     map.setView(e, myZoom);
// }


var person= L.marker([50.7360, -3.5350],{icon: greenIcon});
person.addTo(map);

map
  .locate()
  .on("locationfound", (e) =>
    //person.setLatLng(e.latlng)
    update(e)
  )
  .on("locationerror", () =>
    map.setView([0, 0], 5)
  );
  

// var self = L.marker(e.latlng);
// self.addTo(map);

function update(e){
  person.setLatLng(e.latlng);
  map.setView(e.latlng, myZoom);
}

setInterval(map.locate(), 3000);
