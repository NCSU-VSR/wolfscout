      dojo.require("dijit.layout.BorderContainer");
      dojo.require("dijit.layout.ContentPane");
      dojo.require("esri.map");
      dojo.require("esri.dijit.Popup");
      dojo.require("esri.layers.FeatureLayer");
      
      var map;
      
      function pageReady() {
        var popup = new esri.dijit.Popup({
          fillSymbol: new esri.symbol.SimpleFillSymbol(esri.symbol.SimpleFillSymbol.STYLE_SOLID, new esri.symbol.SimpleLineSymbol(esri.symbol.SimpleLineSymbol.STYLE_SOLID, new dojo.Color([255,0,0]), 2), new dojo.Color([255,255,0,0.25]))
        }, dojo.create("div"));

        
        var initExtent = new esri.geometry.Extent({"xmin":-13626637,"ymin":4550020,"xmax":-13624728,"ymax":4551042,"spatialReference":{"wkid":102100}});
        map = new esri.Map("arc_map",{
          extent:initExtent,
          infoWindow:popup,
          outFields: ["*"]
        });
        
        dojo.addClass(map.infoWindow.domNode, "myTheme");


        dojo.connect(map,"onClick",function(evt){
          var query = new esri.tasks.Query();
          query.geometry = pointToExtent(map,evt.mapPoint,10);
          
          var deferred = featureLayer.selectFeatures(query,esri.layers.FeatureLayer.SELECTION_NEW);

           map.infoWindow.setFeatures([deferred]);
           map.infoWindow.show(evt.mapPoint);
    
        });
        
        //Add the topographic layer to the map. View the ArcGIS Online site for services http://arcgisonline/home/search.html?t=content&f=typekeywords:service    
        var basemap = new esri.layers.ArcGISTiledMapServiceLayer("http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer");
        map.addLayer(basemap);
        
        var incidentLayer = new esri.layers.ArcGISDynamicMapServiceLayer("http://servicesbeta.esri.com/ArcGIS/rest/services/SanFrancisco/SFStreetTreesRendered/MapServer");
        map.addLayer(incidentLayer);
        
               
        var template = new esri.InfoTemplate();
        template.setContent(getTextContent);

        var featureLayer = new esri.layers.FeatureLayer("http://servicesbeta.esri.com/ArcGIS/rest/services/SanFrancisco/SFStreetTreesRendered/MapServer/0",{
          mode: esri.layers.FeatureLayer.MODE_SELECTION,
         outFields: ["*"],
          infoTemplate:template
        });
        
        map.addLayer(featureLayer);

    
        dojo.connect(map, 'onLoad', function(theMap) { 
         //resize the map when the browser resizes
         dojo.connect(dijit.byId('map'), 'resize', map,map.resize);
        });
      }

     function getTextContent(graphic) {
        var attr = graphic.attributes.qSpecies.replace('"',"").split("::");
        var content;
        var scientificName = attr[0];
        //display the common name if it exists - otherwise just the scientific
        if(attr[1]){
          content = "<b>" + dojo.string.trim(attr[1].replace('"',"")) + "</b><br/><i>" + scientificName + "</i>";
        }
        else{
          content = "<i>" + scientificName + "</i>"
        }
        return  content + "<br>" + graphic.attributes.qAddress  + "<br/> Planted on " + formatDate(graphic.attributes.PlantDate);
        
      }
      function formatDate(value){
        var inputDate = new Date(value);
        return dojo.date.locale.format(inputDate, {
          selector: 'date',
          datePattern: 'MMMM d, y' 
        });
      }
      
     function pointToExtent(map, point, toleranceInPixel) {
       var pixelWidth = map.extent.getWidth() / map.width;
       var toleraceInMapCoords = toleranceInPixel * pixelWidth;
       return new esri.geometry.Extent( point.x - toleraceInMapCoords,
                    point.y - toleraceInMapCoords,
                    point.x + toleraceInMapCoords,
                    point.y + toleraceInMapCoords,
                    map.spatialReference );                           
      }
      
      dojo.addOnLoad(pageReady);