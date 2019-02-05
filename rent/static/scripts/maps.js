(function() {
    const map = new google.maps.Map(document.getElementById('map'), {
      center: latlng,
      zoom: 12
    });
    new google.maps.Marker({ position: latlng, map });
  })()