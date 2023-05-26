
/*To get BHK value*/
function getBHK() {
  var bhk = document.getElementsByName("bhk");
  for(var i in bhk) {
    if(bhk[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; 
}

/*To get Bath value*/
function getBath() {
  var bath = document.getElementsByName("bath");
  for(var i in bath) {
    if(bath[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; 
}
/* On the click of Estimate price button*/
function onClickPrice() {
	
  var sqft = document.getElementById("sqft");
  var bhk = getBHK();
  var bath = getBath();
  var location = document.getElementById("locations");
  var estPrice = document.getElementById("estimatedPrice");

   var url = "http://127.0.0.1:5000/predict_home_price";

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bath,
      location: location.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

/*On page load*/
function onPageLoad() {
 
   var url = "http://127.0.0.1:5000/get_location_names"; 
  $.get(url,function(data, status) {
      
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("locations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#locations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;