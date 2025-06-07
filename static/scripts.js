home = document.getElementById("home");
products = document.getElementById("products");
category = document.getElementById("category");
about = document.getElementById("about");


function homeTab(){

}

function productsTab(){

}

function categoryTab(){

}

function aboutTab(){

}

function categoryTab(evt, tabs) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("MobilePhoneAccessories");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabs).style.display = "block";
  evt.currentTarget.className += " active";
}