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

 	//Don't Show password fields if root passwered is checked for all
 	$(".root").change(function(){
 		$(".sub").attr('disabled', this.checked)
 	});

});