data = [
  {
    "lat": 53.800755,
    "lng": -1.549077 ,
    "html": "Leeds" 
  },
  {
    "lat": 51.507351,
    "lng": -0.127758,
    "html": "London" 
  },
   {
    "lat": 54.978252,
    "lng": -1.617780,
    "html": "Newcastle" 
  }
]

function initMap() {

        var center= {lat: data[0].lat, lng: data[0].lng};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 6,
          center: center
        });
var image = {
    url: 'http://goinkscape.com/wp-content/uploads/2015/07/twitter-logo-final.png',
    scaledSize : new google.maps.Size(20, 20)
  };

        var infowindow = null;
        var infowindow = new google.maps.InfoWindow({
          content: "holding"});
        
        for (i = 0; i < 3; i++) {
          var marker = new google.maps.Marker({
          position: {lat: data[i].lat, lng: data[i].lng},
          map: map,
          icon: image,
          html: data[i].html
        });

          google.maps.event.addListener(marker, 'click', function () {
            infowindow.setContent( this.html
            );
            infowindow.open(map, this);
          });   
        };
      }