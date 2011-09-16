      var gmap = null;
      var qtask = null;
      var query = null;
      var mapExtension = null;
      var gOverlays = null;

      function initialize() {
        // GMap construction
        gmap = new GMap2(document.getElementById('arc_map'));
        gmap.addMapType(G_NORMAL_MAP);
        gmap.addMapType(G_SATELLITE_MAP);
        gmap.addControl(new GLargeMapControl());
        gmap.addControl(new GMapTypeControl());
        gmap.setCenter(new GLatLng(33.96964806519751, -117.37674951553345), 17); // RIVERSIDE (Point)
        gmap.enableScrollWheelZoom();


        //Create MapExtension utility class
        mapExtension = new esri.arcgis.gmaps.MapExtension(gmap);


        // Query Task
        qtask = new esri.arcgis.gmaps.QueryTask("http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/Demographics/ESRI_Census_USA/MapServer/0");

        // You can execute a task and listen for the complete event or use the callback to get the results
        GEvent.addListener(qtask, "executecomplete", function() {
          //console.debug("'query task complete' event fired!!!");
        });

        // Query
        query = new esri.arcgis.gmaps.Query();
      }

      function executeQuery() {
        var bounds = gmap.getBounds();

        // clear map overlays and event listeners using MapExtension removeFromMap
        mapExtension.removeFromMap(gOverlays);

        // set query parameters
        query.queryGeometry = bounds;
        query.returnGeometry = true;

        // execute query task
        qtask.execute(query, false, mycallback);

      }

      function mycallback(fset) {
        // add the feature set to google map without any style
        gOverlays = mapExtension.addToMap(fset);
      }