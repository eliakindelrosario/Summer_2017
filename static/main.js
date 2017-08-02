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
			var changeTo = $('#password').val(); // get password value
			// Change all other password values with the root password
			//FIX- Values are not setting
			$('#password_p_usr').val(changeTo);
			$('#password_postgress').val(changeTo);
			$('#tomcat_password').val(changeTo);
			$('#keystore_password').val(changeTo);
			$('#keystore_password_confirm').val(changeTo);
			$('#globus_password').val(changeTo);
		}
	});

	//Handle Tomcat view
	$("#install_tomcat").change(function() {
		var selected = $(this).find(':selected').text();
		console.log(selected);
		// FIX- do noyt display when check_for_all is checked
		if (selected.toLowerCase() == "yes"){
			$('.tom').show();
		} else {
			$('.tom').hide();
		}
	});

	// Handle Globus view
	$("#install_globus").change(function() {
		var selected = $(this).find(':selected').text();
		// FIX- do noyt display when check_for_all is checked
		if (selected.toLowerCase() == "yes"){
			$('.glob').show();
		} else {
			$('.glob').hide();
		}
	});

	// Handle installation type
	$('#esgcet').change(function(){
		var selected = $(this).find(':selected').text();
		console.log(selected)
		// Display options based on the select type
		// Waiting for form breakdown
	//}).change();
	});

	// Handle openId
	$("#openid").change(function() {
		if (this.checked) {
			$('.hide_ob').show();
		} else {
			$('.hide_ob').hide();
		}
	});

	// Handle security schema
	$("#security_schema").change(function() {
		if (this.checked) {
			$('.hide_ss').show();
		} else {
			$('.hide_ss').hide();
		}
	});

	// Submit all the forms with on button 
	submitForms = function(){
    	document.getElementById("form1").submit();
    	document.getElementById("form2").submit();
	}

});