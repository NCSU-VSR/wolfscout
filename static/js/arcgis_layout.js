dojo.require("dijit.dijit"); // optimize: load dijit layer
dojo.require("dijit.layout.BorderContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("esri.map");
dojo.require("esri.dijit.Scalebar");
dojo.require("esri.arcgis.utils");
dojo.require("dijit.layout.StackContainer"); 

dojo.require("esri.layers.FeatureLayer");

var map, urlObject;
var configOptions;

function init() {

	configOptions = {
		webmap:"4b517a5d748d4d66a8926b4cd28c2e17",
		//arcgis.com sharing url is used modify this if yours is different
		sharingurl:"http://arcgis.com/sharing/content/items",
		//enter the bing maps key for your organization if you want to display bing maps
		bingMapsKey:""
	}

	esri.arcgis.utils.arcgisUrl = configOptions.sharingurl;

	//configure map slider to be horizontally place at bottom right
    esriConfig.defaults.map.slider = { right:"70px", bottom:"10px", width:"200px", height:null };

	//get the web map id from the url 
	urlObject = esri.urlToObject(document.location.href);
	urlObject.query = urlObject.query || {};
	if(urlObject.query && urlObject.query.webmap){
		configOptions.webmap = urlObject.query.webmap;
	}

	//create the map using the web map id specified using configOptions or via the url parameter
	var mapDeferred = esri.arcgis.utils.createMap(configOptions.webmap, "arc_map", {
		mapOptions: {
			slider: true,
			nav: false,
			wrapAround180:true
		},
		ignorePopups:false,
		bingMapsKey: configOptions.bingMapsKey
	});

	mapDeferred.addCallback(function (response) {
		//map title and subtitle
		dojo.byId("arc_title").innerHTML = configOptions.title ||response.itemInfo.item.title;
		dojo.byId("arc_subtitle").innerHTML = configOptions.subtitle || response.itemInfo.item.snippet || "";
	    dojo.byId("arc_description").innerHTML = configOptions.description || response.itemInfo.item.description || "";
		map = response.map;
		if(map.loaded){
			initUI();
		}else{
			dojo.connect(map,"onLoad",function(){
				initUI();
			});
		}       
	});

	mapDeferred.addErrback(function (error) {
		console.log("CreateMap failed: ", dojo.toJson(error));
	});

}

function initUI(){   
	//resize the map when the browser resizes
	dojo.connect(dijit.byId('arc_map'), 'resize', map,map.resize);        
	//add scalebar or other components like a legend, overview map etc
	var scalebar = new esri.dijit.Scalebar({
		map: map,
		scalebarUnit:"english" 
	});    
}
        
//show map on load 
dojo.addOnLoad(init);