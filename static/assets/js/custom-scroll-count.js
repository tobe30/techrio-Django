/*==========

Template Name: Shivaa

==========*/

/*==========
----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Counting JS
==========*/



$(document).ready(function($) {

	// Whole Script Strict Mode Syntax
	"use strict";

	var a = 0;
	var b = 0;
	$(window).on('scroll', function() {
	// Counting JS Start
		var oTop = $('#progress_bar').offset().top - window.innerHeight;
		if (a === 0 && $(window).scrollTop() > oTop) {
			$('.counting').each(function() {
			  var $this = $(this),
			      countTo = $this.attr('data-count');
			  
			  $({ countNum: $this.text()}).animate({
			    countNum: countTo
			  },

			  {

			    duration: 2000,
			    easing:'linear',
			    step: function() {
			      $this.text(Math.floor(this.countNum));
			    },
			    complete: function() {
			      $this.text(this.countNum);
			    }

			  });  
			  
			});
		a = 1;
	  	}
		var oTop2 = $('#progress_bar').offset().top - window.innerHeight;
		if (b === 0 && $(window).scrollTop() > oTop2) {
			$(".counter-bar").each(function(){
				$(this).find(".counter-bar-inner").animate({
					width: $(this).attr("data-width")
				},2000);
			});
		}
	// Counting JS Start

	});

});