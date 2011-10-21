dojo.require("dijit.layout.BorderContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("esri.map");
dojo.require("esri.layers.FeatureLayer");

    var map, baseMapLayer, featureLayer;

    var baseMapUrl = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer";
  
    var featureLayerUrl = "http://sampleserver3.arcgisonline.com/ArcGIS/rest/services/Petroleum/KSPetro/MapServer/1";
    //var featureLayerUrl = "http://localhost:8000/rest/collarDataResource/1/";

    function init() {
        var extent = new esri.geometry.Extent({"xmin":-102,"ymin":36,"xmax":-95,"ymax":41,"spatialReference":{"wkid":4269}});
        extent = esri.geometry.geographicToWebMercator(extent);

        //configure map slider to be horizontally place at bottom right
        esriConfig.defaults.map.slider = { left:"10px", bottom:"10px", width:"250px", height:null };
        
        map = new esri.Map("arc_map", {extent: extent});
        
        dojo.connect(map, "onLoad", mapLoaded);
        
        dojo.connect(map,"onUpdateStart",function(){
            esri.show(dojo.byId("status"));
        });
        
        dojo.connect(map,"onUpdateEnd",function(){
            esri.hide(dojo.byId("status"));
        });

        // base map
        baseMapLayer = new esri.layers.ArcGISTiledMapServiceLayer(baseMapUrl);
        map.addLayer(baseMapLayer);
    }
    
    /*function mapLoaded() {
        //resize the map when the browser resizes
        dojo.connect(dijit.byId('arc_map'), 'resize', map,map.resize);
        var maxOffset = function maxOffset(map, pixelTolerance) {
        return Math.floor(map.extent.getWidth() / map.width) * pixelTolerance;
    };*/
    
    var content = "<b>Status</b>: ${STATUS}" +
        "<br><b>Cummulative Gas</b>: ${CUMM_GAS} MCF" +
        "<br><b>Total Acres</b>: ${APPROXACRE}" +
        "<br><b>Avg. Field Depth</b>: ${AVG_DEPTH} meters";
    var infoTemplate = new esri.InfoTemplate("${FIELD_NAME}", content);
    
    dojo.addClass(map.infoWindow.domNode, "myTheme");

    dojo.connect(map,"onClick",function(evt){
      var query = new esri.tasks.Query();
      query.geometry = pointToExtent(map,evt.mapPoint,10);

      var deferred = featureLayer.selectFeatures(query,esri.layers.FeatureLayer.SELECTION_NEW);

       map.infoWindow.setFeatures([deferred]);
       map.infoWindow.show(evt.mapPoint);

    });
    
    featureLayer = new esri.layers.FeatureLayer(featureLayerUrl, {
        mode: esri.layers.FeatureLayer.MODE_ONDEMAND,
        infoTemplate: infoTemplate,
        outFields: ["*"],
        maxAllowableOffset: maxOffset(map,1)
    });
    
    dojo.connect(featureLayer, "onLoad", function() {
        dojo.connect(map, "onZoomEnd", function() {
            featureLayer.setMaxAllowableOffset(maxOffset(map,1));
        });
    });

    dojo.connect(featureLayer, "onUpdateStart", function() {
        dojo.style(dojo.byId("status"), "display", "");
    });

    dojo.connect(featureLayer, "onUpdateEnd", function() {
        dojo.style(dojo.byId("status"), "display", "none");
    });

    map.addLayers([featureLayer]);
    
    }
    
    function toggleLayer(val){
        if(val.name === 'checkBM'){
            (val.checked) ? baseMapLayer.show() : baseMapLayer.hide();
        }
        if(val.name === 'checkFL'){
            (val.checked) ? featureLayer.show() : featureLayer.hide();
        } 
    }
    
    dojo.addOnLoad(init);