data = [
  {
    "lat": -25.363,
    "lng": 131.044 ,
    "html": "Hello" 
  },
  {
    "lat": -31.950527,
    "lng": 115.860457,
    "html": "Hello2" 
  },
   {
    "lat": -29.950527,
    "lng": 115.860457,
    "html": "Hello3" 
  }
]



function initMap() {

        var center= {lat: data[0].lat, lng: data[0].lng};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: center
        });

        var infowindow = null;
        var infowindow = new google.maps.InfoWindow({
          content: "holding"});
        
        for (i = 0; i < 3; i++) {
          var marker = new google.maps.Marker({
          position: {lat: data[i].lat, lng: data[i].lng},
          map: map,
          html: data[i].html
        });

          google.maps.event.addListener(marker, 'click', function () {
            infowindow.setContent( this.html
            );
            infowindow.open(map, this);
          });   
        };
      }