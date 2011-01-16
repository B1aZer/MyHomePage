(function($) {

    $.extend({

        make: function(){
			var $elem,text,children,type,name,props;
			var args = arguments;
			var tagname = args[0];
			if(args[1]){
				if (typeof args[1]=='string'){
					text = args[1];
				}else if(typeof args[1]=='object' && args[1].push){
				  children = args[1];
				}else{
					props = args[1];
				}
			}
			if(args[2]){
				if(typeof args[2]=='string'){
					text = args[2];
				}else if(typeof args[1]=='object' && args[2].push){
				  children = args[2];
				}
			}
			if(tagname == 'text' && text){
			    return document.createTextNode(text);
			}else{
    			$elem = $(document.createElement(tagname));
    			if(props){
    				for(var propname in props){
    				  if (props.hasOwnProperty(propname)) {
    				        if($elem.is(':input') && propname == 'value'){
    				            $elem.val(props[propname]);
    				        } else {
    				            $elem.attr(propname, props[propname]);
    				        }
    					}
    				}
    			}
    			if(children){
    				for(var i=0;i<children.length;i++){
    					if(children[i]){
    						$elem.append(children[i]);
    					}
    				}
    			}
    			if(text){
    				$elem.html(text);
    			}
    			return $elem;
    		}
		}

	});
})(jQuery);

$(function() {
        $(document).ready(function () {
        //$("body").layout();
        $("body").layout({});
        //$("#content-container").layout({ applyDefaultStyles: true });
            });
        callback = function(data) {
            for (row in data) {
                console.log(data);
                var fields = data[row].fields;
                //console.log(fields)
            }
            
        }
        make_request = function(url, data, callback) {
        $.ajax({
            url: url,
            data: data,
            type: 'POST',
            success: function(o) {
                //var data = eval('(' + o + ')');
                if(callback && typeof callback == 'function'){
                    callback(data);
                }
            }
        });    
        };
        
        /*var $feed = $.make('div', { className: 'feed' }, [*/
        /*$.make('span', { className: 'unread_count' }, ''),feeds[f].unread_count),*/
        /*$.make('img', { className: 'feed_favicon', src: self.google_favicon_url + feeds[f].feed_link }),*/
        /*$.make('span', { className: 'feed_title' }, feeds[f].feed_title),*/
        /*$.make('span', { className: 'feed_id' }, ''+feeds[f].id)*/
        /*]);*/
//ver1 working
        var $feed = $.make('div', { className: 'accordeon' }, [
                //$.make('h3').html('Title'),[
                $.make('h3',{}, [
                    $.make('a', { className: 'title', href: "#"}).html('link')
                    ]),// folders[fo].folder),
                $.make('div', { className: 'entry' }, [
                        $.make('div', { className: 'profile' }, [
                            $.make('a', { href: '#'}, [
                                $.make('img', { src: '#'})
                                ]).html('inner link'),
                            ]),
                        $.make('div', { className: 'body' }, [
                            $.make('div', { className: 'message' }, [
                                $.make('a', { className: 'name' , href: '#'}).html('link name')
                                ]),
                            $.make('div', { className: 'created' }).html('created ago')
                            ]),
                        ]),
                ]);

        //$('<h1>').html('Timeline').appendTo('#content');
        //$('#content').append($feed);


        $( "a", "#aside" ).button();
        $( "a", "#aside" ).click(function() { 
            //$.getJSON('b.json');
            /*$.post("/json/", {type: "json"},*/
            /*function(data) {*/
            /*callback(data);*/
            /*}, "json");*/
            //var i = 0
 //ver2 working           

            /*$( '#content' ).load('/add/', {*/
            /*limit: '5',*/
            /*//begin: i+5*/
            /*}, function() {*/
            /*$( ".accordeon" ).accordion({*/
            /*collapsible: true,*/
            /*active: false*/
            /*});*/
            /*});*/
            //hm = $('.integer').text();
            var system = $(this).text();
            if (!$('.integer').text()){
                var hm = 0;
                //alert('not')
            }else{
                hm = $('.integer').text()
            }

            $.ajax({
                type: "POST",
                url: "/add/",
                data: {
                    limit: '10',
                    inter: hm,
                    system:system
                },
                success: function(html){
                $("#content").empty();
                $("#content").append(html);
                //$(html).hide().appedTo("#content").show();
                /*$(html).appedTo("#content");*/
                /*$(html)*/
                /*// Sets the style of the elements to "display:none"*/
                /*//  .hide()*/
                /*// Appends the hidden elements to the "posts" element*/
                /*.appendTo('#content')*/
                /*// Fades the new content into view*/
                /*// .fadeIn();*/
                /*.parent()*/
                /*.hide()*/
                /*.show('slow')*/

                //
                $( ".accordeon" ).accordion({
                    collapsible: true,
                    active: false
                });
                    $('.integer').hide();

                    
                    //hm = $('.integer').text();
                    //$('.integer').remove();

                   // if (!$('.integer').text()){
                    //    hm = 0            
                    //}else{
                        //$('.integer').remove();
                    //}

                }
            });
                        
            /*make_request('/add/',*/
            /*{*/
            /*limit: 5*/
            /*}, */
            /*callback);*/

            /*$.post(url, $("#some_form").serialize(), function(data, text_status){*/
            /*alert(data);*/
            /*}, "json");*/
            
        });

        /*var request =  make_request('/test/mark_story_as_read');*/
        /*{*/
        /*story_id: story_id*/
        /*}, callback*/
        /*);*/
        
        //	$( "#toggle" ).button().toggle(function() {
        //		$( "#accordion" ).accordion( "option", "icons", false );
        //		}, function() {
        //		$( "#accordion" ).accordion( "option", "icons", icons );
        //	});
	});

