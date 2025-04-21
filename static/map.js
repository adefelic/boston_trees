const initial_coords = [42.360, -71.065]; // https://leafletjs.com/reference.html#latlng
const initial_zoom = 14;
const mapId = 'map';
const map = L.map(mapId, {
	center: initial_coords,
	zoom: initial_zoom
});

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


addTreesLayer();

async function getTreesGeoJson() {
	const url = 'trees';
	try {
		const response = await fetch(url);
		if (!response.ok) {
			throw new Error(`Response status: ${response.status}`);
		}
		const json = await response.json();
		return json;
	} catch (error) {
		console.log(error.message);
	}
}

async function addTreesLayer() {
	const trees = await getTreesGeoJson();
	var totalCount = 0;
	var nativeCount = 0;

	L.geoJson(trees, {
		filter: function(feature) {
			totalCount++;
			if (feature.properties.native) {
				nativeCount++;
				return true;
			}
			return false;
		}
	}).addTo(map)
	console.log(nativeCount + "/" + totalCount);
}
