$('document').ready(function() {
   $('#fullpage').fullpage({
    anchors: ['first_page', 'second_page'],
            sectionsColor : ['#fbf8f5', '#343a40'],
    css3: true,
                scrollingSpeed: 1000,
                navigation: true,
                slidesNavigation: true,
                controlArrows: false,
                scrollbars: true,
                scrollOverflow: true, // even though this is set to true, it's not working// even though this is set to true, it's not working
                // Navigation

  // Scrolling

 

         });


setTimeout(function(){
    $.fn.fullpage.reBuild();
}, 100);

$("#button-7day").click(function() {
                fullpage_api.moveTo('second_page', 1);
              
              });
function initialize() {
                var input = document.getElementById('searchTextField');
                var autocomplete = new google.maps.places.Autocomplete(input);
                google.maps.event.addListener(autocomplete, 'place_changed', function () {
                    var place = autocomplete.getPlace();
                    document.getElementById('city2').value = place.name;
                    document.getElementById('cityLat').value = place.geometry.location.lat();
                    document.getElementById('cityLng').value = place.geometry.location.lng();
            
                    //alert("This function is working!");
                    //alert(place.name);
                   // alert(place.address_components[0].long_name);
            
                });
            }
            google.maps.event.addDomListener(window, 'load', initialize); 


});

