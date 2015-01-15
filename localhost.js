doctitle = document.title;
var pathArray = window.location.pathname.split( '/' );
var newPort = window.location.port;
var newPathname = window.location.hostname+":"+newPort;

for ( i = 1; i < pathArray.length - 1; i++ ) {
  newPathname += "/";
  newPathname += pathArray[i];
}
addr = newPathname;

function createChart(instr) {
	if (instr === undefined){ instr = "container"}
	//$("#"+instr).width($(window).width()-100);
	//console.log('bb '+instr);
	//console.log(seriesOptions);
	window.chart = new Highcharts.StockChart({
		chart : {
			renderTo : instr
		},
		title : {
			text : doctitle
		},
		xAxis : {
			maxZoom : 1 * 24 * 3600000 // fourteen days
		},
		series : seriesOptions
	});
};

function addZero(inVal) {
	var ret;
    		if(inVal.toString().length < 2){
        		ret = "0" + inVal;
    		}
    		else {
    			ret = inVal;
   		};
	return ret;
}

function DateToSQL(inDate) {
	var ret, curdate, curmonth, curyear, curhour, curmin, cursec;
	curday 		= inDate.getDate();
	curmonth 	= inDate.getMonth();
	curyear 	= inDate.getFullYear();
	curhour 	= inDate.getHours();
	curmin 		= inDate.getMinutes();
	cursec 		= inDate.getSeconds();
	ret = '' + curyear + addZero(curmonth+1) + addZero(curday) + addZero(curhour) + addZero(curmin) + addZero(cursec);
    //var format = new SimpleDateFormat("yyyyMMddHHmmss");
    //ret = format.format(inDate);
	return ret;
}

(function( $ ){
    $.fn.myBkg = function(  ) {  
	return this.each(function() {

    	    var $this = $(this);

	    $this.addClass( "ui-accordion" );
	    $this.find( "h2:first" )
		.addClass( "ui-accordion-header ui-helper-reset ui-state-active ui-corner-all" );
	    //headers = $this.find("h3:first").addClass( "ui-accordion-header ui-helper-reset ui-state-active ui-corner-top" );;
	    headers = $this.find("h3").addClass( "ui-accordion-header ui-helper-reset ui-state-active ui-corner-top" );
	    //console.log(headers);
	    //headers = $this.find( "> li > :first-child,> :not(li):even" );
	    //console.log(headers);
		//.addClass( "ui-accordion-header ui-helper-reset ui-state-active ui-corner-top" );
	    headers.next()
		.addClass( "ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom" );
	});
    };

})( jQuery );

