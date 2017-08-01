$(document).ready(function(){
 	console.log("Hello World!")

 	//Change page forward
 	$(".next").on("click", function(){
 		if($('.page.active').index() < $(".page").length-1)
 			$('.page.active').removeClass("active").next().addClass("active");
 		console.log("Move Forward. Index:"+$('.page.active').index())
 	});

 	//Change page backward
 	$(".prev").on("click", function(){
 		if($('.page.active').index() > 0)
 			$('.page.active').removeClass("active").prev().addClass("active");
 		console.log("Move Backward. Index:"+$('.page.active').index())
 	});

 	// Activate popover event
 	$('[data-toggle="popover"]').popover();

 	//Don't Show password fields if root password is checked for all
 	$(".root").change(function(){
 		$(".sub").attr('disabled', this.checked)
 	});

 	// Hide all password fields if checked
	$("#complete_with_root_pass").change(function() {
		if (!this.checked) {
			$('#password_p_usr').show();
			$('#password_postgress').show();
			$('#tomcat_password').show();
			$('#keystore_password').show();
			$('#keystore_password_confirm').show();
			$('#globus_password').show();
		} else {
			$('#password_p_usr').hide();
			$('#password_postgress').hide();
			$('#tomcat_password').hide();
			$('#keystore_password').hide();
			$('#keystore_password_confirm').hide();
			$('#globus_password').hide();
			//TODO - ADD rootpassword value to these fields
		}
	});

});