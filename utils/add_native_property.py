import fiona
from fiona import Feature, Properties, Geometry

# script for adding the boolean "native" property to treekeeper_street_trees.geojson

# interpretation of native for this project:
# - has to exist natively in new england.
# - cultivars of native plants don't count.
# sources are: "native plants of the northeast", gobotany, usda, wikipedia

native_trees_from_book = [
	"Abies balsamea",
	"Acer nigrum",
	"Acer pensylvanicum",
	"Acer rubrum",
	"Acer saccharum",
	"Aesculus flava",
	"Aesculus glabra",
	"Aesculus pavia",
	"Aesculus sylvatica",
	"Amelanchier arborea",
	"Aralia spinosa",
	"Asimina triloba",
	"Betula alleghaniensis",
	"Betula lenta",
	"Betula nigra",
	"Betula papyrifera",
	"Betula populifolia",
	"Carpinus caroliniana",
	"Carya illinoinensis",
	"Carya laciniosa",
	"Carya ovata",
	"Celtis occidentalis",
	"Cercis canadensis",
	"Chamaecyparis thyoides",
	"Cladrastis kentukea",
	"Cornus alternifolia",
	"Cornus florida",
	"Cotinus obovatus",
	"Crataegus crus-galli",
	"Crataegus mollis",
	"Crataegus phaenopyrum",
	"Crataegus punctata",
	"Crataegus viridis",
	"Diospyros virginiana",
	"Fagus grandifolia",
	"Fraxinus americana",
	"Fraxinus nigra",
	"Fraxinus pennsylvanica",
	"Fraxinus quadrangulata",
	"Gleditsia triacanthos",
	"Gymnocladus dioicus",
	"Halesia carolina",
	"Ilex montana",
	"Ilex opaca",
	"Juniperus virginiana",
	"Larix laricina",
	"Liquidambar styraciflua",
	"Liriodendron tulipfera",
	"Magnolia acuminata",
	"Magnolia fraseri",
	"Magnolia macrophylla",
	"Magnolia tripetala",
	"Magnolia virginiana",
	"Malus coronaria",
	"Malus angustifolia",
	"Malus ioensis",
	"Malus glaucescens",
	"Nyssa sylvatica",
	"Ostrya virginiana",
	"Oxydendrum arboreum",
	"Picea glauca",
	"Picea mariana",
	"Pinus banksiana",
	"Pinus echinata",
	"Pinus resinosa",
	"Pinus rigida",
	"Pinus strobus",
	"Pinus virginiana",
	"Platanus occidentalis",
	"Populus deltoides",
	"Populus grandidentata",
	"Populus tremuloides",
	"Prunus americana",
	"Prunus pensylvanica",
	"Ptelea trifoliata",
	"Quercus alba",
	"Quercus coccinea",
	"Quercus imbricaria",
	"Quercus laurifolia",
	"Quercus lyrata",
	"Quercus macrocarpa",
	"Quercus muehlenbergii",
	"Quercus palustris",
	"Quercus phellos",
	"Quercus prinus",
	"Quercus rubra",
	"Quercus shumardii",
	# "Robinia pseudoacacia", # prohibited/invasive in MA?
	"Salix amygdaloides",
	"Salix discolor",
	"Salix nigra",
	"Sassafras albidum",
	"Sorbus americana",
	"Stewartia ovata",
	"Styrax americanus",
	"Taxodium distichum",
	"Thuja occidentalis",
	"Tilia americana",
	"Tsuga canadensis",
	"Viburnum lentago",
	"Viburnum prunifolium",
	"Viburnum rufidulum",
]
native_trees_bot_from_dataset = ['Acer saccharinum', 'Acer x freemanii', 'Amelanchier canadensis', 'Amelanchier laevis', 'Carya cordiformis', 'Cercis canadensis var. alba', 'Hamamelis virginiana', 'Juglans cinerea', 'Juglans nigra', 'Liriodendron tulipifera', 'Morus rubra', 'Myrica cerifera', 'Prunus pennsylvanica', 'Prunus virginiana', 'Quercus bicolor', 'Quercus montana', 'Quercus velutina', 'Quercus x schuettei', 'Sambucus canadensis', 'Ulmus rubra']
nativars = ["Acer rubrum 'Armstrong'", "Acer rubrum 'October Glory'", "Acer rubrum 'Red Sunset'", "Acer saccharum 'Green Mountain'", "Amelanchier laevis 'Cumulus'", "Amelanchier laevis 'Snowcloud'", "Crataegus viridis 'Winter King'", "Picea glauca 'Conica'", "Prunus virginiana 'Canada Red'", "Quercus bicolor 'Bonnie and Mike'Quercus palustris 'Pringreen'", "Quercus palustris 'Fastigiata'", 'Ulmus americana', "Ulmus americana 'Princeton'", "Ulmus americana 'Valley Forge'", "Ulmus americana 'jefferson'", "Ulmus minor 'Christine Buisman'"]
insufficient_data = ['Acer species', 'Amelanchier species', 'Amelanchier spp.', 'Carya species', 'Celtis species', 'Cornus species', 'Corylus species', 'Crataegus species', 'Euonymus species', 'Fagus species', 'Fraxinus species', 'Hydrangea species', 'Juniperus species', 'Magnolia species', 'Malus species', 'Malus spp.', 'Morus species', 'Picea species', 'Prunus species', 'Quercus species', 'Quercus x', 'Salix species', 'Taxus species', 'Thuja species', 'Tilia species', 'Ulmus species', 'Ulmus x', 'Viburnum species']
confirmed_not_native = ['Acer barbatum', 'Acer campestre', "Acer campestre 'Queen Elizabeth'", 'Acer ginnala', 'Acer griseum', 'Acer miyabei', "Acer miyabei 'Morton'", 'Acer negundo', 'Acer palmatum', 'Acer platanoides', "Acer platanoides 'Columnar'", "Acer platanoides 'Crimson King'", "Acer platanoides 'Schwedleri'", 'Acer pseudoplatanus', 'Acer tataricum', 'Acer truncatum', "Acer truncatum x platanoides 'Keithsform'", 'Aesculus hippocastanum', 'Aesculus x carnea', 'Ailanthus altissima', 'Albizia julibrissin', 'Betula pendula', 'Broussonetia papyrifera', 'Carpinus betulus', "Carpinus betulus 'Fastigiata'", "Carpinus betulus 'Franz Fontaine'", 'Casuarina equisetifolia', 'Catalpa speciosa', 'Cedrus atlantica', 'Celtis sinensis', 'Cercidiphyllum japonicum', 'Chamaecyparis obtusa', 'Chionanthus virginicus', 'Cornus kousa', 'Cornus mas', 'Cornus x rutgersensis', 'Corylus colurna', 'Crataegus laevigata', 'Cryptomeria japonica', 'Cupressocyparis leylandii', 'Eucommia ulmoides', "Fagus sylvatica 'Atropunicea'", 'Fagus sylvaticaPlatycladus orientalis', 'Fraxinus angustifolia', 'Ginkgo biloba', 'Gleditsia triacanthos inermis', 'Halesia tetraptera', 'Hibiscus syriacus', 'Koelreuteria paniculata', "Koelreuteria paniculata 'Gocanzam'", 'Laburnum anagyroides', 'Laburnum x watereri', 'Lagerstroemia indica', 'Larix decidua', "Liquidambar styraciflua 'Fastigiata'", "Liquidambar styraciflua 'Happdell'", 'Maackia amurensis', 'Magnolia denudata', 'Magnolia kobus', 'Magnolia stellata', 'Magnolia x loebneri', 'Magnolia x soulangiana', "Malus 'Golden Raindrops'", "Malus 'JFS-KW5'", "Malus 'Sugartyme'", "Malus 'Sutyzam'", 'Malus pumila', "Malus x 'Snowdrift'", 'Metasequoia glyptostroboides', 'Morus alba', 'Parrotia persica', 'Phellodendron amurense', 'Photinia species', 'Picea abies', 'Picea pungens', "Picea pungens 'Glauca'", 'Pinus mugo', 'Pinus nigra', 'Platanus x acerifolia', 'Populus alba', "Prunus 'Okame'", 'Prunus amygdalus', 'Prunus avium', 'Prunus cerasifera', "Prunus cerasifera 'Thundercloud'", 'Prunus maackii', 'Prunus padus', 'Prunus pendula', 'Prunus persica', 'Prunus sargentii', 'Prunus serotina', 'Prunus serrulata', "Prunus serrulata 'Kwanzan'", "Prunus serrulata 'Shirotae'", 'Prunus subhirtella', "Prunus subhirtella 'Autumnalis'", 'Prunus x cistena', 'Prunus x yedoensis', 'Prunus yedoensis', 'Pseudotsuga menziesii', 'Pyrus calleryana', "Pyrus calleryana 'Bradford'", "Pyrus calleryana 'Chanticleer'", 'Pyrus species', 'Pyrus ussuriensis', 'Quercus acutissima', 'Quercus ellipsoidalis', 'Quercus marilandica', 'Quercus petraea', 'Quercus robur', 'Quercus robur f. fastigiata', 'Quercus robur x bicolor', "Quercus x warei 'Long'", 'Rhamnus cathartica', 'Rhamnus frangula', 'Salix alba', 'Salix gracilistyla', 'Sciadopitys verticillata', 'Sequoia sempervirens', 'Sequoiadendron giganteum', 'Sophora japonica', "Sophora japonica 'Halka'", 'Stewartia pseudocamellia', 'Styphnolobium japonicum', 'Styrax japonicus', "Syringa pekinensis 'China Snow'", 'Syringa reticulata', 'Syringa species', 'Tilia cordata', "Tilia cordata 'Greenspire'", 'Tilia platyphyllos', 'Tilia tomentosa', 'Ulmus alata', 'Ulmus carpinifolia', "Ulmus carpinifolia 'Hollandica'", "Ulmus carpinifolia 'accolade'", 'Ulmus davidiana', 'Ulmus parvifolia', 'Ulmus procera', 'Ulmus pumila', 'Ulmus serotina', 'Ulmus thomasii', 'Ulmus wilsoniana', "Ulmus x 'Frontier'", 'Zelkova serrata', "Zelkova serrata 'Green Vase'", "Zelkova serrata 'Musashino'", 'Zelkova species']
invalid = [
	"Vacant Unacceptable/Retired",
	"Scheduled Planting Site - Spring 2025",
	"Empty Pit/Planting Site",
	"--",
	"Vacant site medium",
	"Vacant site small",
	"Stump"
]

natives = native_trees_from_book + native_trees_bot_from_dataset
with fiona.open("static/data/treekeeper_street_trees.geojson") as src:

	# copy source schema, add new property
	dst_schema = src.schema
	dst_schema["properties"]["native"] = "bool"

	# uniques_not_in_list = set()
	# uniques_in_list = set()

	# for feat in src:
	# 	# print(feat.properties["spp_bot"])
	# 	spp_bot = feat.properties["spp_bot"]
	# 	if spp_bot not in native_trees_bot:
	# 		uniques_not_in_list.add(spp_bot)
	# 	else:
	# 		uniques_in_list.add(spp_bot)

	# print("not in list:")
	# for x in uniques_not_in_list:
	# 	print(x)
	# print("\nin list:")
	# for x in uniques_in_list:
	# 	print(x)


	with fiona.open(
		"static/data/boston_trees.geojson",
		mode="w",
		crs=src.crs,
		driver="GeoJSON",
		schema=dst_schema
	) as dst:
		for feat in src:
			isNative = False;
			if feat.properties['spp_bot'] in natives:
				isNative = True

			props = Properties.from_dict(
				**feat.properties,
				native=isNative
			)

			dst.write(Feature(geometry=feat.geometry, properties=props))
