$(document).ready(function(){

  $('body').on('click', '#list_name p', function(){
    $('#list_name p').removeClass("btn_active");
    $(this).addClass("btn_active");
    var mql1 = window.matchMedia('all and (max-width: 575px)');
    var wrapper = $('#navigation');
    var nsc = $(document).scrollTop();
    var bp1 = wrapper.offset().top;
      if (mql1.matches) {
        $("#list_name").hide();
     		if (nsc<bp1) {
     		$("#nav_user").css({"background": ""});
     		}
     	if (nsc<bp1) {
     		$("#nav_user").css({"position": "relative"});
     			}
      }


    $.get("users/user_owned/", {cmd: 'user', index: $(this).attr("id") }, function(data) {
       $("#block_all_info").remove();
       $("#block_user_info").remove();
       $('#block_info').append(data);
    });
  });

  $('body').on('click', '.header_log', function(){
    $.get("users/user_owned/", {cmd: 'all'}, function(data) {
      $("#block_all_info").remove();
      $("#block_user_info").remove();
      $('#block_info').append(data);
    });
  });

  $('body').on('click', '#bth_rfid', function(){
    if ($('#bth_rfid').text() == "Добавить") {

      $("#add_rfid").show();
      $("#add_rf").hide(); $('#bth_rf').text("Добавить");
      $("#add_finger").hide(); $('#bth_finger').text("Добавить");

      $('#bth_rfid').text("Отмена")
    } else if ($('#bth_rfid').text() == "Отмена") {
      $("#add_rfid").hide();
      $('#bth_rfid').text("Добавить");
    }
  });

    $('body').on('click', '#bth_rf', function(){
      if ($('#bth_rf').text() == "Добавить") {

        $("#add_rfid").hide(); $('#bth_rfid').text("Добавить");
        $("#add_rf").show();
        $("#add_finger").hide(); $('#bth_finger').text("Добавить");

        $('#bth_rf').text("Отмена")
      } else if ($('#bth_rf').text() == "Отмена") {
        $("#add_rf").hide();
        $('#bth_rf').text("Добавить");
      }
    });

      $('body').on('click', '#bth_finger', function(){
        if ($('#bth_finger').text() == "Добавить") {

          $("#add_rfid").hide(); $('#bth_rfid').text("Добавить");
          $("#add_rf").hide(); $('#bth_rf').text("Добавить");
          $("#add_finger").show();

          $('#bth_finger').text("Отмена")
        } else if ($('#bth_finger').text() == "Отмена") {
          $("#add_finger").hide();
          $('#bth_finger').text("Добавить");
        }

    //$.get("users/user_owned/", {cmd: 'all'}, function(data) {
    //  $("#block_all_info").remove();
    //  $("#block_user_info").remove();
    //  $('#block_info').append(data);
    //});
  });

});