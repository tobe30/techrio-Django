/*==========

Template Name: Shivaa

==========*/

/*==========
----- JS INDEX -----

1. Gallery- Swiper

==========*/



$(document).ready(function($) {
    if ($('.galley-thumb-swiper').length > 0 && $('.galley-swiper').length > 0) {
		var swiper = new Swiper(".galley-thumb-swiper", {
		  loop: false,
		  spaceBetween: 10,
		  slidesPerView: 4,
		  freeMode: true,
		  watchSlidesProgress: true,
		});
	
		var swiper2 = new Swiper(".galley-swiper", {
		  loop: true,
		  spaceBetween: 10,
		  thumbs: {
			swiper: swiper,
		  },
		});
	}

    if (jQuery('.status-swiper').length > 0) {
        var Statusswiper = new Swiper('.status-swiper', {
            loop: true,
            spaceBetween: 0,
            slidesPerView: "auto",
            speed: 1500,
            effect: "fade",
            autoplay: {
                delay: 2000,
            },
            pagination: {
                el: ".status-pagination",
                clickable: true,
            },
        });

        
        jQuery('.post-status-btn').on('click', function () {
            Statusswiper.slideTo(0); 
            Statusswiper.autoplay.start(); 
        });
    }



    if(jQuery('.blog-slideshow').length > 0){
			var swiperTestimonial = new Swiper('.blog-slideshow', {
				loop: true,
				spaceBetween: 0,
				slidesPerView: "auto",
				speed: 1500,
				//autoplay: {
				//   delay: 2000,
				//},
				pagination: {
				  el: ".swiper-pagination-two",
				  clickable: true,
				},
			});
		}
});