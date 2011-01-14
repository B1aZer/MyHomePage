	$(function() {
        $(document).ready(function () {
        //$("body").layout();
        $("body").layout({});
        //$("#content-container").layout({ applyDefaultStyles: true });
            });

		var icons = {
			header: "ui-icon-circle-arrow-e",
			headerSelected: "ui-icon-circle-arrow-s"
		};
		$( ".accordeon" ).accordion({
			collapsible: true,
            active: false
		});
        $( "a", "#aside" ).button();
        $( "a", "#aside" ).click(function() { return false; });
        
	//	$( "#toggle" ).button().toggle(function() {
	//		$( "#accordion" ).accordion( "option", "icons", false );
    //		}, function() {
	//		$( "#accordion" ).accordion( "option", "icons", icons );
	//	});
	});

