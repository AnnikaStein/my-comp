function toggleLang() {
  var german = document.getElementById("main-de");
  var english = document.getElementById("main-en");

  var lang_divs = [german, english];

  for (i=0; i < lang_divs.length; i++) {
    if (lang_divs[i].classList.contains("hidden")) {
      lang_divs[i].style.display = "block";
    } else {
      lang_divs[i].style.display = "none";
    }
    lang_divs[i].classList.toggle("hidden");
  }
}
