function toggleLang() {
  var german = document.getElementById("main-de");
  var english = document.getElementById("main-en");

  var german2 = document.getElementById("main-de-2");
  var english2 = document.getElementById("main-en-2");

  if (german2.classList.contains("navi")) {
    var lang_divs = [german2, english2];
  }
  else {
    var lang_divs = [german, english];
  }

  for (i=0; i < lang_divs.length; i++) {
    if (lang_divs[i].classList.contains("hidden")) {
      lang_divs[i].style.display = "block";
    } else {
      lang_divs[i].style.display = "none";
    }
    lang_divs[i].classList.toggle("hidden");
  }
}

// Merci https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API/Using_the_Geolocation_API
function locate() {

  function success(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    console.log(latitude);
    console.log(longitude);

    var [lati1, long1] = [50.049303, 10.211571];
    // this is just an arbitrary test, to be replaced of course whenever this becomes relevant
    var [lati2, long2] = [-50.049303, -10.211571];

    // Taken from https://www.htmlgoodies.com/javascript/calculate-the-distance-between-two-points-in-your-web-apps/
    // (The Haversine function to calc distance on sphere, assuming km is the unit for output and inputs are in degree)
    function distance(lat1, lon1, lat2, lon2) {
        var radlat1 = Math.PI * lat1/180;
        var radlat2 = Math.PI * lat2/180;
        var radlon1 = Math.PI * lon1/180;
        var radlon2 = Math.PI * lon2/180;
        var theta = lon1 - lon2;
        var radtheta = Math.PI * theta/180;
        var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
        dist = Math.acos(dist);
        dist = dist * 180/Math.PI;
        dist = dist * 60 * 1.1515;
        dist = dist * 1.609344;
        return dist
    }

    let firstDist = distance(latitude, longitude, lati1, long1);
    let secondDist = distance(latitude, longitude, lati2, long2);

    // if second comp is closer:
    if (secondDist < firstDist) {
      console.log("Second comp is closer");
      var german_far = document.getElementById("main-de");
      var english_far = document.getElementById("main-en");

      var german_closer = document.getElementById("main-de-2");
      var english_closer = document.getElementById("main-en-2");
    }
    else {
      console.log("First comp is closer");
      var german_closer = document.getElementById("main-de");
      var english_closer = document.getElementById("main-en");

      var german_far = document.getElementById("main-de-2");
      var english_far = document.getElementById("main-en-2");
    }

    let lang_divs_far = [german_far, english_far];
    let lang_divs_closer = [german_closer, english_closer];

    for (i=0; i < lang_divs_far.length; i++) {
      lang_divs_far[i].style.display = "none";
      lang_divs_far[i].classList.remove("navi");
    }

    for (i=0; i < lang_divs_closer.length; i++) {
      lang_divs_closer[i].classList.add("navi");
    }
    german_closer.style.display = "block";
  }

  function error() {
    console.log("Unable to retrieve your location");
  }

  if (!navigator.geolocation) {
    console.log("Geolocation is not supported by your browser");
  } else {
    console.log("Waiting for GPS location ...");
    navigator.geolocation.getCurrentPosition(success, error);
  }
}

// comment out when there is only one comp the given weekend
locate();
