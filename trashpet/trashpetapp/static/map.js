
const layer = L.tileLayer(url, {
  attribution: copy,
});
const map = L.map("map", {
  layers: [layer],
  
}).setView([51.505, -0.09], 13);

var marker = L.marker([51.5, -0.09]).addTo(map);