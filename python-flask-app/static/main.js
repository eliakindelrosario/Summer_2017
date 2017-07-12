$(document).ready(function(){
 	console.log("Hello World!")

 	//Change page forward
 	$('.next').on("click", function(){
 		if($('.page.active').index() < $(".page").length-1)
 			$('.page.active').removeClass("active").next().addClass("active");
 		console.log("Move Forward. Index:"+$('.page.active').index())
 	});

 	//Change page backward
 	$('.prev').on("click", function(){
 		if($('.page.active').index() > 0)
 			$('.page.active').removeClass("active").prev().addClass("active");
 		console.log("Move Backward. Index:"+$('.page.active').index())
 	});

});