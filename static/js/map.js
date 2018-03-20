function initMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var Perth = {lat: -31.950527, lng: 115.860457}
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
        var marker = new google.maps.Marker({
          position: Perth,
          map: map
        });
      }