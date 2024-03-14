// when there is only one comp the given weekend
//var duoCompWeekend = false;
// switch to true if you want to locate the user or ask for manual selection
var duoCompWeekend = true;

// usually, trivial case with only one comp per weekend
var timeDependent = false;
// if multiple comps are happening for a given location (series comp)
//var timeDependent = true;

function toggleLang() {
  var german = document.getElementById("main-de-0");
  var english = document.getElementById("main-en-0");

  if (duoCompWeekend) {
    var german2 = document.getElementById("main-de-1");
    var english2 = document.getElementById("main-en-1");

    if (german2.classList.contains("navi")) {
      var lang_divs = [german2, english2];
    }
    if (german.classList.contains("navi")) {
      var lang_divs = [german, english];
    }
    if (timeDependent) {
      var german3 = document.getElementById("main-de-2");
      var english3 = document.getElementById("main-en-2");
      if (german3.classList.contains("navi")) {
        var lang_divs = [german3, english3];
      }
    }
  } else {
    var lang_divs = [german, english];
  }

  for (i = 0; i < lang_divs.length; i++) {
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

    // Delmenhorst
    //var [lati1, long1] = [53.048325, 8.628512];
    // Gütersloh
    var [lati1, long1] = [51.884364, 8.366529];
    // Nürnberg (series comp)
    var [lati2, long2] = [49.49267, 11.24286];

    // Taken from https://www.htmlgoodies.com/javascript/calculate-the-distance-between-two-points-in-your-web-apps/
    // (The Haversine function to calc distance on sphere, assuming km is the unit for output and inputs are in degree)
    function distance(lat1, lon1, lat2, lon2) {
      var radlat1 = (Math.PI * lat1) / 180;
      var radlat2 = (Math.PI * lat2) / 180;
      var radlon1 = (Math.PI * lon1) / 180;
      var radlon2 = (Math.PI * lon2) / 180;
      var theta = lon1 - lon2;
      var radtheta = (Math.PI * theta) / 180;
      var dist =
        Math.sin(radlat1) * Math.sin(radlat2) +
        Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
      dist = Math.acos(dist);
      dist = (dist * 180) / Math.PI;
      dist = dist * 60 * 1.1515;
      dist = dist * 1.609344;
      return dist;
    }

    let firstDist = distance(latitude, longitude, lati1, long1);
    let secondDist = distance(latitude, longitude, lati2, long2);
    let thirdDist = secondDist;

    // if second comp is closer:
    if (secondDist < firstDist) {
      console.log("Second comp is closer");
      var german_far = document.getElementById("main-de-0");
      var english_far = document.getElementById("main-en-0");

      if (timeDependent) {
        // From https://stackoverflow.com/a/30776817/22745629
        var d = new Date();
        console.log(d.toUTCString());
        // Monday = 1, Saturday = 6, Sunday = 0 - don't ask why
        if (d.getUTCHours() >= 14 || d.getUTCDay() == 0) {
          console.log("Take later comp (B)");
          var german_closer = document.getElementById("main-de-2");
          var english_closer = document.getElementById("main-en-2");
          var german_far2 = document.getElementById("main-de-1");
          var english_far2 = document.getElementById("main-en-1");
        } else {
          console.log("Take earlier comp (A)");
          var german_closer = document.getElementById("main-de-1");
          var english_closer = document.getElementById("main-en-1");
          var german_far2 = document.getElementById("main-de-2");
          var english_far2 = document.getElementById("main-en-2");
        }
      } else {
        var german_closer = document.getElementById("main-de-1");
        var english_closer = document.getElementById("main-en-1");
      }
    } else {
      console.log("First comp is closer");
      var german_closer = document.getElementById("main-de-0");
      var english_closer = document.getElementById("main-en-0");

      var german_far = document.getElementById("main-de-1");
      var english_far = document.getElementById("main-en-1");
      if (timeDependent) {
        var german_far2 = document.getElementById("main-de-2");
        var english_far2 = document.getElementById("main-en-2");
      }
    }
    let lang_divs_far;
    if (timeDependent) {
      lang_divs_far = [german_far, english_far, german_far2, english_far2];
    } else {
      lang_divs_far = [german_far, english_far];
    }
    let lang_divs_closer = [german_closer, english_closer];

    for (i = 0; i < lang_divs_far.length; i++) {
      lang_divs_far[i].style.display = "none";
      lang_divs_far[i].classList.remove("navi");
    }

    for (i = 0; i < lang_divs_closer.length; i++) {
      lang_divs_closer[i].classList.add("navi");
    }
    german_closer.style.display = "block";
  }

  function error() {
    console.log("Unable to retrieve your location");
    openManualLocModal();
  }

  if (!navigator.geolocation) {
    console.log("Geolocation is not supported by your browser");
    openManualLocModal();
  } else {
    console.log("Waiting for GPS location ...");
    navigator.geolocation.getCurrentPosition(success, error);
  }
}
function openManualLocModal() {
  var selectionModal = document.getElementById("selectionModal");
  selectionModal.style.display = "block";
}
function manualCompSelector(ind) {
  var selectionModal = document.getElementById("selectionModal");
  selectionModal.style.display = "none";
  // TIL how to use switch case in vanilla JS https://stackoverflow.com/a/6514571/22745629
  switch (ind) {
    case "0":
      console.log("First comp was chosen");
      var german_closer = document.getElementById("main-de-0");
      var english_closer = document.getElementById("main-en-0");

      var german_far = document.getElementById("main-de-1");
      var english_far = document.getElementById("main-en-1");
      var german_far2 = document.getElementById("main-de-2");
      var english_far2 = document.getElementById("main-en-2");
      break;
    case "1":
      console.log("Second comp was chosen");
      var german_closer = document.getElementById("main-de-1");
      var english_closer = document.getElementById("main-en-1");

      var german_far = document.getElementById("main-de-0");
      var english_far = document.getElementById("main-en-0");
      var german_far2 = document.getElementById("main-de-2");
      var english_far2 = document.getElementById("main-en-2");
      break;
    case "2":
      console.log("Third comp was chosen");
      var german_closer = document.getElementById("main-de-2");
      var english_closer = document.getElementById("main-en-2");

      var german_far = document.getElementById("main-de-0");
      var english_far = document.getElementById("main-en-0");
      var german_far2 = document.getElementById("main-de-1");
      var english_far2 = document.getElementById("main-en-1");
      break;
  }

  let lang_divs_far = [german_far, english_far, german_far2, english_far2];
  let lang_divs_closer = [german_closer, english_closer];

  for (i = 0; i < lang_divs_far.length; i++) {
    lang_divs_far[i].style.display = "none";
    lang_divs_far[i].classList.remove("navi");
  }

  for (i = 0; i < lang_divs_closer.length; i++) {
    lang_divs_closer[i].classList.add("navi");
  }
  german_closer.style.display = "block";
}

if (duoCompWeekend) {
  locate();
}
