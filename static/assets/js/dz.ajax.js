/*
Abstract : Ajax Page Js File
File : dz.ajax.js
#CSS attributes: 
	.dzForm : Form class for ajax submission. 
	.dzFormMsg  : Div Class| Show Form validation error/success message on ajax form submission

#Javascript Variable
.dzRes : ajax request result variable
.dzFormAction : Form action variable
.dzFormData : Form serialize data variable

*/

function contactForm()
{
	window.verifyRecaptchaCallback = function (response) {
        $('input[data-recaptcha]').val(response).trigger('change');
    }

    window.expiredRecaptchaCallback = function () {
        $('input[data-recaptcha]').val("").trigger('change');
    }
	'use strict';
	var msgDiv;
	$(".dzForm").submit(function(e)
	{
		e.preventDefault();	//STOP default action
		$('.dzFormMsg').html('<div class="gen alert alert-success">submitted successfully! We will get back to you in the next 24 hours</div>');
		var dzFormAction = $(this).attr('action');
		var dzFormData = $(this).serialize();
		
		$.ajax({
			method: "POST",
			url: dzFormAction,
			data: dzFormData,
			dataType: 'json',
			success: function(dzRes){
				
				if(dzRes.status == 1){
					msgDiv = '<div class="gen alert alert-success">'+dzRes.msg+'</div>';
				}
				
				if(dzRes.status == 0){
					msgDiv = '<div class="err alert alert-danger">'+dzRes.msg+'</div>';
				}
				
				$('.dzFormMsg').html(msgDiv);
				
				setTimeout(function(){
					$('.dzFormMsg .alert').hide(1000);
				}, 10000);
				
				$('.dzForm')[0].reset();
                grecaptcha.reset();
				
				
			}
		})
	});
	
	
	
	
	
	/* This function is for mail champ subscription START*/
	
	$(".dzSubscribe").submit(function(e)
	{
		e.preventDefault();	//STOP default action
		var dzFormAction = $(this).attr('action');
		var dzFormData = $(this).serialize();
		$.ajax({
			method: "POST",
			url: dzFormAction,
			data: dzFormData,
			dataType: 'json',
		  success: function(dzRes) {
			if(dzRes.status == 1){
				msgDiv = '<p style="color: #34A853">'+dzRes.msg+'</p>';
			}
			if(dzRes.status == 0){
				msgDiv = '<p style="color: #EA4335">'+dzRes.msg+'</p>';
			}
			$('.dzSubscribeMsg').html(msgDiv);
			$('.dzSubscribe')[0].reset();
		  }
		})
	});
	
	setInterval(function(){
		$('.dzSubscribeMsg p').hide(1000);
	}, 5000);
	
	/* This function is for mail champ subscription END*/
	
}







jQuery(document).ready(function() {
    'use strict';
	contactForm();
})	