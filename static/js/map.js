//Load in the Data from python
data = test


function initMap() {
        //define the center of tha map
        var center= {lat: data[0].lat, lng: data[0].lng};
        //use google API to load the map - links to the HTML div using 'map'
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 6,
          center: center
        });

        //Loads the twitter logo to use as a marker on the map
        var image = {
          url: 'http://goinkscape.com/wp-content/uploads/2015/07/twitter-logo-final.png',
          scaledSize : new google.maps.Size(20, 20)
        };

        //create the pop-up window
        var infowindow = null;
        var infowindow = new google.maps.InfoWindow({
          content: "holding"});
        
        //creates the markers for locations in the loaded data
        for (i = 0; i < 3; i++) {
          var marker = new google.maps.Marker({
          position: {lat: data[i].lat, lng: data[i].lng},
          map: map,
          icon: image,
          html: data[i].html
        });

          //opens the pop-up window on click
          google.maps.event.addListener(marker, 'click', function () {
            infowindow.setContent( this.html
            );
            infowindow.open(map, this);
          });   
        };
      }