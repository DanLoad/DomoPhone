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


    $.get("users/user_owned/", {cmd: 'user', user: $(this).attr("id") }, function(data) {
       $("#block_all_info").remove();
       $("#block_user_info").remove();
       $('#block_info').append(data);
    });
  });

  $('body').on('click', '.header_log', function(){
    $.get("users/all_owned/", {cmd: 'all'}, function(data) {
      $("#block_all_info").remove();
      $("#block_user_info").remove();
      $('#block_info').append(data);
    });
  });


//Добавить
  $('body').on('click', '#bth_rfid', function(){
    if ($('#bth_rfid').text() == "Добавить") {

      $("#add_rfid").show();
      $("#add_rf").hide(); $('#bth_rf').text("Добавить");
      $("#add_finger").hide(); $('#bth_finger').text("Добавить");
      $('#bth_rfid').text("Отмена");

      $.get("users/rfid_owned/", {cmd: 'add', user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });



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
        $('#bth_rf').text("Отмена");

        $.get("users/rf_owned/", {cmd: 'add', user: $(".btn_active").attr("id") }, function(data) {
           alert(data);
         });

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
          $('#bth_finger').text("Отмена");

        } else if ($('#bth_finger').text() == "Отмена") {
          $("#add_finger").hide();
          $('#bth_finger').text("Добавить");
        }
      });


//Удалить
      $('body').on('click', '.delete_rfid', function(){
        if(confirm("Вы действительно хотите удалить?")) {
            $.get("users/rfid_owned/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
           });
        }
      });

      $('body').on('click', '.delete_rf', function(){
        if(confirm("Вы действительно хотите удалить?")) {
            $.get("users/rf_owned/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
           });
        }
      });

      $('body').on('click', '.delete_finger', function(){
        if(confirm("Вы действительно хотите удалить?")) {
            $.get("users/finger_owned/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
           });
        }
      });


//Актевировать - Деактевировать
      $('body').on('click', '.change_activ_rfid', function(){
            $.get("users/rfid_owned/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
           });
      });

      $('body').on('click', '.change_activ_rf', function(){
            $.get("users/rf_owned/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
           });
      });

      $('body').on('click', '.change_activ_finger', function(){
            $.get("users/finger_owned/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
           });
      });



});
