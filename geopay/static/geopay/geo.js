var MapAPIKey = 'AIzaSyDmDY1vCJXWHMcFHMS3_eKly8iZn4dor_U';
var GeocodingAPIKey = 'AIzaSyDpN2zxO9oanQp53skHdScbC51TqbYTRbE';

function Geo() {
    this.currentLocation = {};
    this.nearbyLocs = {};
    var self = this;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            self.currentLocation.lat = position.coords.latitude;
            self.currentLocation.lng = position.coords.longitude;
        });
    }
}

Geo.prototype = {
    /**
     * @param {object} options Options for search
     * e.g. `{
     *   type: 'cafe',
     *   radius: '50',
     *   keyword: 'vegetarian'
     * }`
     }
     */
    search: function(request) {
        if (!request.location) {
            console.log(this.currentLocation.lat, this.currentLocation.lng);
            request.location = new google.maps.LatLng(this.currentLocation.lat, this.currentLocation.lng);
        }
        var service = new google.maps.places.PlacesService(document.createElement('div'));
        var self = this;

        service.radarSearch(request, function(results) {
            self.nearbyLocs.length = results.length;

            for (var i = 0; i < results.length; i++) {
                var result = results[i];
                self.nearbyLocs[result.place_id] = {
                    lat: result.lat,
                    lng: result.lng
                };

                service.getDetails({
                    placeId: result.place_id
                }, function(place) {
                    self.nearbyLocs[result.place_id].name = place.name;
                });
            }
        });
    }
};

