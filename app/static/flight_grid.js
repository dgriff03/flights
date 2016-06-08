ORIGIN = 'SFO';

$( document ).ready(function() {
    var numDates = $('.date-headers').length;
    var airports = Array.prototype.map.call($('#airport-codes span'),
                                            function(node) {return node.innerHTML;});
    for (var i = 0; i < numDates; ++i) {
        for (var j = 0; j < airports.length; ++j) {
            (function (airport, index) {
                $.get( 'flights.json',
                    {origin: ORIGIN,
                     destination: airport,
                     offset: index,
                     }).done(function( data ) {
                        var jsonData = JSON.parse(data);
                        var waitTime = Math.round(Math.random() * 10000);
                        setTimeout(function() {
                            var queryString = buildQueryString(airport, index);
                            var cells = $(queryString);
                            for (var k = 0; k < cells.length; ++k) {
                                placePriceLink(cells[k], jsonData['price'], jsonData['link'])
                            }
                        }, waitTime);
                     });
            })( airports[j], i)
        }
    }
});

function placePriceLink(cell, price, link) {
    cell.innerHTML = '<a href="' + link + ' target="_blank">$' + price + '</a>';
}

function buildQueryString(aiport, index){
    return 'tr[data-airport="' + aiport + '"] td[data-index="' + index + '"]';
}