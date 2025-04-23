const initial_coords = [42.360, -71.065]; // https://leafletjs.com/reference.html#latlng
const initial_zoom = 14;
const mapId = 'map';

const map = L.map(mapId, {
	preferCanvas: true,
	center: initial_coords,
	zoom: initial_zoom
});

const color_by_spp_bot = new Map([
	['Abies balsamea', '#530381'],
	['Acer nigrum', '#bc1fd1'],
	['Acer pensylvanicum', '#e906d2'],
	['Acer rubrum', '#881ff6'],
	['Acer saccharinum', '#7217e1'],
	['Acer saccharum', '#f8c47e'],
	['Acer x freemanii', '#9f590a'],
	['Aesculus flava', '#9af83f'],
	['Aesculus glabra', '#e33409'],
	['Aesculus pavia', '#6806c2'],
	['Aesculus sylvatica', '#05e36b'],
	['Amelanchier arborea', '#9afb43'],
	['Amelanchier canadensis', '#38c1c5'],
	['Amelanchier laevis', '#aa2e41'],
	['Aralia spinosa', '#9997d3'],
	['Asimina triloba', '#bdb690'],
	['Betula alleghaniensis', '#681629'],
	['Betula lenta', '#81aa66'],
	['Betula nigra', '#5b00e3'],
	['Betula papyrifera', '#e16d1d'],
	['Betula populifolia', '#2f3def'],
	['Carpinus caroliniana', '#be6978'],
	['Carya cordiformis', '#02be91'],
	['Carya illinoinensis', '#11f5dc'],
	['Carya laciniosa', '#6ab202'],
	['Carya ovata', '#4ee2b3'],
	['Celtis occidentalis', '#a05d21'],
	['Cercis canadensis', '#bf4e87'],
	['Cercis canadensis var. alba', '#77d65d'],
	['Chamaecyparis thyoides', '#923c47'],
	['Cladrastis kentukea', '#1d4e7d'],
	['Cornus alternifolia', '#2e48b7'],
	['Cornus florida', '#926b58'],
	['Cotinus obovatus', '#bac4ad'],
	['Crataegus crus-galli', '#48149f'],
	['Crataegus mollis', '#fc1c55'],
	['Crataegus phaenopyrum', '#27175b'],
	['Crataegus punctata', '#d28166'],
	['Crataegus viridis', '#a2ee9d'],
	['Diospyros virginiana', '#590c99'],
	['Fagus grandifolia', '#36ada8'],
	['Fraxinus americana', '#978053'],
	['Fraxinus nigra', '#d6fe8c'],
	['Fraxinus pennsylvanica', '#331465'],
	['Fraxinus quadrangulata', '#4dbe16'],
	['Gleditsia triacanthos', '#3493aa'],
	['Gymnocladus dioicus', '#d4e575'],
	['Halesia carolina', '#a258e7'],
	['Hamamelis virginiana', '#0e10ab'],
	['Ilex montana', '#3d4a1f'],
	['Ilex opaca', '#d3032b'],
	['Juglans cinerea', '#012327'],
	['Juglans nigra', '#c849e2'],
	['Juniperus virginiana', '#817b64'],
	['Larix laricina', '#bc2fb3'],
	['Liquidambar styraciflua', '#851ba5'],
	['Liriodendron tulipfera', '#2d85bb'],
	['Liriodendron tulipifera', '#1206c9'],
	['Magnolia acuminata', '#4ab58a'],
	['Magnolia fraseri', '#f53adc'],
	['Magnolia macrophylla', '#ff86d0'],
	['Magnolia tripetala', '#c08e32'],
	['Magnolia virginiana', '#20f85a'],
	['Malus angustifolia', '#b7811b'],
	['Malus coronaria', '#f73ca3'],
	['Malus glaucescens', '#241491'],
	['Malus ioensis', '#655d3e'],
	['Morus rubra', '#c94ec8'],
	['Myrica cerifera', '#afe55f'],
	['Nyssa sylvatica', '#bc989b'],
	['Ostrya virginiana', '#990175'],
	['Oxydendrum arboreum', '#70c7e3'],
	['Picea glauca', '#4861f0'],
	['Picea mariana', '#0fe7c0'],
	['Pinus banksiana', '#f95884'],
	['Pinus echinata', '#e95382'],
	['Pinus resinosa', '#99d587'],
	['Pinus rigida', '#3ffe7e'],
	['Pinus strobus', '#f1f6d4'],
	['Pinus virginiana', '#50a455'],
	['Platanus occidentalis', '#07c9ef'],
	['Populus deltoides', '#063b71'],
	['Populus grandidentata', '#75334a'],
	['Populus tremuloides', '#0b563a'],
	['Prunus americana', '#dae41c'],
	['Prunus pennsylvanica', '#6d7ca9'],
	['Prunus pensylvanica', '#016af2'],
	['Prunus virginiana', '#efe196'],
	['Ptelea trifoliata', '#1f0c86'],
	['Quercus alba', '#8ebc1a'],
	['Quercus bicolor', '#feaacc'],
	['Quercus coccinea', '#868617'],
	['Quercus imbricaria', '#5ca6b1'],
	['Quercus laurifolia', '#65aab2'],
	['Quercus lyrata', '#9a6605'],
	['Quercus macrocarpa', '#cce7ec'],
	['Quercus montana', '#b3f02e'],
	['Quercus muehlenbergii', '#3fefad'],
	['Quercus palustris', '#67c340'],
	['Quercus phellos', '#919739'],
	['Quercus prinus', '#087846'],
	['Quercus rubra', '#7ec688'],
	['Quercus shumardii', '#d97e42'],
	['Quercus velutina', '#3e86c3'],
	['Quercus x schuettei', '#77b924'],
	['Salix amygdaloides', '#2244f4'],
	['Salix discolor', '#a79601'],
	['Salix nigra', '#8a7640'],
	['Sambucus canadensis', '#54608f'],
	['Sassafras albidum', '#0f3cac'],
	['Sorbus americana', '#ee4151'],
	['Stewartia ovata', '#c82112'],
	['Styrax americanus', '#205a7a'],
	['Taxodium distichum', '#1b694a'],
	['Thuja occidentalis', '#fd87ff'],
	['Tilia americana', '#869fd5'],
	['Tsuga canadensis', '#3e4b70'],
	['Ulmus rubra', '#dd9dc9'],
	['Viburnum lentago', '#7d634d'],
	['Viburnum prunifolium', '#3dc919'],
	['Viburnum rufidulum', '#6e7db1']
]);


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
		},
		onEachFeature: function(feature, layer) {
			layer.bindPopup(feature.properties.spp_com);
		},
		pointToLayer: function(feature, latlng) {
			return new L.CircleMarker(latlng);
		},
		style: function(feature) {
			return {
				color: color_by_spp_bot.get(feature.properties.spp_bot)
			};
		},
	}).addTo(map);
	console.log(nativeCount + "/" + totalCount);
}
