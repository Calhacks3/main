var MapAPIKey = 'AIzaSyDmDY1vCJXWHMcFHMS3_eKly8iZn4dor_U';
var GeocodingAPIKey = 'AIzaSyDpN2zxO9oanQp53skHdScbC51TqbYTRbE';
var PlacesAPIKey = 'AIzaSyBlV3_PXnd5Dx0kB8BxSmmTQ_IGHUapmJ0';

function initialize(geoObj) {
    var geocoder = new google.maps.Geocoder();
    if (google.loader.ClientLocation) {
        geoObj.currentLocation.lat = google.loader.ClientLocation.latitutde;
        geoObj.currentLocation.lng = google.loader.ClientLocation.longitude;

        var latlng = new google.maps.LatLng(geoObj.lat, geoObj.lng);
        geocoder.geocode({ latlng: latlng }, function(results, status) {
            if (status != google.maps.GeocoderStatus.OK) {
                console.log(results);
            }
        });
    }
}

function Geo() {
    this.currentLocation = {};
    this.nearbyLocs = {};

    google.load('maps', '3.x', {
        other_params: 'sensor=false',
        callback: initialize
    });
}

Geo.prototype = {
    nearbyAddress: {},

    baseSearchURL: 'https://maps.googleapis.com/maps/api/place/radarsearch/json?',

    /**
     * @param {object} options Options for search
     * e.g. `{
     *   type: 'cafe',
     *   radius: '50',
     *   keyword: 'vegetarian'
     * }`
     }
     */
    search: function(options) {
        var params = '';
        var searchURL = this.baseSearchURL;
        var self = this;
        // build request url
        for (var prop in options) {
            if (options.hasOwnProperty(prop)) {
                params += prop + '=' + options[prop] + '&';
            }
        }

        searchURL += 'location=' + this.currentLocation.lat + ',' + this.currentLocation.lng + '&';
        searchURL += 'key=' + PlacesAPIKey;

        // make request
        $.ajax({
            method: 'GET',
            url: searchURL,
            dataType: 'application/json',
            success: function(response) {
                var data = JSON.parse(response);
                var results = data.results;
                for (var i = 0; i < results.length; i++) {
                    self.nearbyLocs[results[i].name] = results[i].geometry;
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    },

    geocodeLocation: function(location) {
        // we may not need this
        // it seems search already returns coordinates
    }
};

module.exports = Geo;
