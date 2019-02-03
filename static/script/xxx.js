$(document).ready(function(){

	$("#contNew").hide();
	$("#contUser").hide();

	var navbar =  $('.side_left');
	var wrapper = $('.navigation');

	$.get("../php/user.php", {}, function(data){
		data = JSON.parse(data);

		for(var id in data) {

			$('<p>', {
				text: data[id],
				id: ("index_" + id),
				class: "bar_name"
			}).appendTo('#spol_id');
		}

	});


 $('.spoiler_links').click(function(){
	var nsc = $(document).scrollTop();
    var bp1 = wrapper.offset().top;
	var display = $("#spol_id").css("display");

	if (display == 'none') {

	$("#spol_id").show();
	$("#side_left").css({"position": "fixed"});
	$("#side_left").css({"top": "0"});
	$("#side_left").css({"background": "rgba(0,105,105,1)"});

	} else {

		$("#spol_id").hide();
		if (nsc<bp1) {
		$("#side_left").css({"background": "rgba(0,255,255,0.14)"});
		}
	if (nsc<bp1) {
		$("#side_left").css({"position": "relative"});
			}
	}
 });



	$(window).scroll(function(){
		if(adaption_scrol()) {
			var nsc = $(document).scrollTop();
			var bp1 = wrapper.offset().top;
			var bp2 = bp1 + wrapper.outerHeight()-$(window).height();
			var show = $("#side_left").css("display");

			if (nsc>bp1) {
				navbar.css('position','fixed');
				$("#side_left").css({"background": "rgba(0,105,105,1)"});
			}
			else {
				if(show == 'none') {
					navbar.css('position','relative');
					$("#side_left").css({"background": "rgba(0,255,255,0.14)"});
				}
			}
			if (nsc>bp2) {

			}
			else {
				navbar.css('top', '0');
			}
		}
	});


});

$(document).on("click", ".spoiler_body p ", function() {

	if($(this).attr("class") == "bar_name") {
		//отправить индекс
		$.get("../php/user.php", {type: 1, index: $(this).attr("id") }, function(data) {
			data = JSON.parse(data);
			$("#name").text(data["name"]);


		});
	}
	var navbar =  $('.side_left');
	var wrapper = $('.navigation');

	var IdButton = $(this).attr('id');
	if (IdButton == "newUrer") {
		$("#contNew").show();
		$("#contUser").hide();
	} else {
		$("#contUser").show();
		$("#contNew").hide();
	}

	var numberIndex = $(this).index();
	var nsc = $(document).scrollTop();
	var bp1 = wrapper.offset().top;

	if (!$(this).is("active")) {
		$(".spoiler_body p").removeClass("active");
		$(this).addClass("active");

	}

	var mql21 = window.matchMedia('all and (max-width: 480px)');
	var mql22 = window.matchMedia('all and (max-width: 768px)');
		if (mql21.matches || mql22.matches) {
			$("#spol_id").fadeOut(300);
		}
	if (nsc<bp1) {
		document.getElementById("side_left").style.position = 'relative';
		document.getElementById("side_left").style.background = 'rgba(0,255,255,0.14)';
	}
});

                 // Адаптация дисплея
window.onresize = function(event) {
	adaption_display();
};
$(document).ready(function($) {
	adaption_display();
});


function adaption_display() {
	var mql1 = window.matchMedia('all and (max-width: 480px)');
	var mql2 = window.matchMedia('all and (max-width: 768px)');
	var mql3 = window.matchMedia('all and (max-width: 992px)');
	var mql4 = window.matchMedia('all and (min-width: 993px)');
	if (mql1.matches || mql2.matches) {
		$("#link_id").show();
		$("#spol_id").hide();
		return true;
	} else if (mql3.matches || mql4.matches) {
		$("#spol_id").show();
		$("#link_id").hide();
		return false;
	} else {return false;}
}

function adaption_scrol() {
	var mql1 = window.matchMedia('all and (max-width: 480px)');
	var mql2 = window.matchMedia('all and (max-width: 768px)');
	var mql3 = window.matchMedia('all and (max-width: 992px)');
	var mql4 = window.matchMedia('all and (min-width: 993px)');

	if (mql1.matches || mql2.matches) {
		return true;
	} else if (mql3.matches || mql4.matches) {
		return false;
	} else {return false;}
}
