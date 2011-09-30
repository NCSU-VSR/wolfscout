dojo.require("esri.map");
      dojo.require("esri.tasks.query");
      dojo.require("esri.toolbars.draw");
      dojo.require("dojox.color.Palette");
      dojo.require("esri.layers.FeatureLayer");
      dojo.require("dojox.grid.DataGrid");
      dojo.require("dojo.data.ItemFileReadStore");
      dojo.require("dijit.layout.BorderContainer");
      dojo.require("dijit.layout.ContentPane");
 
      var map, wellFeatureLayer, toolbar, grid, store, resizeTimer;
 
      function init() {
          //configure map slider to be horizontally place at bottom right
          esriConfig.defaults.map.slider = { right:"70px", bottom:"10px", width:"200px", height:null };
          
        var startExtent = new esri.geometry.Extent(-97.5328,37.4344,-97.2582,37.64041, new esri.SpatialReference({wkid:4326}) );
 
        map = new esri.Map("arc_map", {extent:esri.geometry.geographicToWebMercator(startExtent)});
        dojo.connect(map, "onLoad", initTopQueryFunctionality);
        var tiledLayer = new esri.layers.ArcGISTiledMapServiceLayer("http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer");
        map.addLayer(tiledLayer);
 
        var imageParams = new esri.layers.ImageParameters();
        imageParams.layerIds = [0,1];
        imageParams.layerOption = esri.layers.ImageParameters.LAYER_OPTION_SHOW;
        var dynamicLayer = new esri.layers.ArcGISDynamicMapServiceLayer("http://sampleserver3.arcgisonline.com/ArcGIS/rest/services/Petroleum/KSPetro/MapServer", {imageParameters:imageParams});
        map.addLayer(dynamicLayer);
 
        var selectionSymbol = new esri.symbol.SimpleMarkerSymbol().setColor("red");
        wellFeatureLayer = new esri.layers.FeatureLayer("http://sampleserver3.arcgisonline.com/ArcGIS/rest/services/Petroleum/KSPetro/MapServer/0", {
          mode: esri.layers.FeatureLayer.MODE_SELECTION,
          infoTemplate: new esri.InfoTemplate("Well: ${API_NUMBER}","${*}")
        });
        wellFeatureLayer.setSelectionSymbol(selectionSymbol);
        dojo.connect(wellFeatureLayer, "onSelectionComplete", findRelatedRecords);
 
        map.addLayer(wellFeatureLayer);
 
        dojo.connect(map, "onClick", findWells);
      }
 
      function initTopQueryFunctionality(map) {
        dojo.connect(dijit.byId('arc_map'), 'resize', function() {
          resizeMap();
        });
      }
 
      function findRelatedRecords(features) {
        var relatedTopsQuery = new esri.tasks.RelationshipQuery();
        relatedTopsQuery.outFields = ["*"];
        relatedTopsQuery.relationshipId = 3;
        relatedTopsQuery.objectIds = [features[0].attributes.OBJECTID];
        
        //Query the feature layer to find related records that meet the input query (relatedTopsQuery).
        wellFeatureLayer.queryRelatedFeatures(relatedTopsQuery, function(relatedRecords) {
          var fset = relatedRecords[features[0].attributes.OBJECTID];
          
          //return an array of feature attributes to provide to the dojo data store.
          var items = dojo.map(fset.features, function(feature) {
            return feature.attributes;
          });
          //Create data object to be used in store
          var data = {
            identifier: "OBJECTID",  //This field needs to have unique values
            label: "OBJECTID", //Name field for display. Not pertinent to a grid but may be used elsewhere.
            items: items
          };
 
          //Create data store and bind to grid.
          store = new dojo.data.ItemFileReadStore({ data:data });
          grid.setStore(store);
          grid.setQuery({ OBJECTID: '*' });
        });
      }
 
      function findWells(evt) {
        grid.setStore(null);
        var selectionQuery = new esri.tasks.Query();
        var tol = map.extent.getWidth()/map.width * 5;
        var x = evt.mapPoint.x;
        var y = evt.mapPoint.y;
        var queryExtent = new esri.geometry.Extent(x-tol,y-tol,x+tol,y+tol,evt.mapPoint.spatialReference);
        selectionQuery.geometry = queryExtent;
        wellFeatureLayer.selectFeatures(selectionQuery,esri.layers.FeatureLayer.SELECTION_NEW);
      }
 
      //Handle resize of browser
      function resizeMap(){
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function(){
          map.resize();
          map.reposition();
        }, 500);
      }

      dojo.addOnLoad(init);