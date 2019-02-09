var index = "off";
var turn = 0;
var step = "off";
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
      console.log("1");
      $("#add_rfid").show();
      $("#add_rf").hide(); $('#bth_rf').text("Добавить");
      $("#add_finger").hide(); $('#bth_finger').text("Добавить");
      $('#bth_rfid').text("Отмена");
      console.log("2");


      $.get("users/rfid_owned/", {cmd: 'add_start', user: $(".btn_active").attr("id") }, function(data) {
        console.log("g1");
        console.log(data);
        $('#rfid_info').text(data);
      });

       console.log("3");
       turn = 14;
       index = "rfid_on"

       console.log("end");
    } else if ($('#bth_rfid').text() == "Отмена") {
      $("#add_rfid").hide();
      $('#bth_rfid').text("Добавить");
    }
    });   //Добавить RFID

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
  });   //Добавить RF

  $('body').on('click', '#bth_finger', function(){
    if ($('#bth_finger').text() == "Добавить") {
      console.log("1");
      $("#add_rfid").hide(); $('#bth_rfid').text("Добавить");
      $("#add_rf").hide(); $('#bth_rf').text("Добавить");
      $("#add_finger").show();
      $('#bth_finger').text("Отмена");

      $.get("users/finger_owned/", {cmd: 'add_start', user: $(".btn_active").attr("id") }, function(data) {
        console.log("g1");
        console.log(data);
        $('#finger_info').text(data);
      });

      console.log("3");
      turn = 14;
      index = "finger_on"

      console.log("end");

    } else if ($('#bth_finger').text() == "Отмена") {
      $("#add_finger").hide();
      $('#bth_finger').text("Добавить");
      turn = 0;
      index = "off"
      $.get("users/finger_owned/", {cmd: 'add_cancel', user: $(".btn_active").attr("id") }, function(data) {
        $("#block_all_info").remove();
        $("#block_user_info").remove();
        $('#block_info').append(data);
      });
    }
  });   //Добавить Finger


//Удалить
  $('body').on('click', '.delete_rfid', function(){
    if(confirm("Вы действительно хотите удалить?")) {
        $.get("users/rfid_owned/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
    }
  });   //Удалить RFID

  $('body').on('click', '.delete_rf', function(){
    if(confirm("Вы действительно хотите удалить?")) {
        $.get("users/rf_owned/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
    }
  });   //Удалить RF

  $('body').on('click', '.delete_finger', function(){
    if(confirm("Вы действительно хотите удалить?")) {
        $.get("users/finger_owned/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
    }
  });   //Удалить Finger


//Актевировать - Деактевировать
  $('body').on('click', '.change_activ_rfid', function(){
        $.get("users/rfid_owned/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
  });   //Деактевировать RFID

  $('body').on('click', '.change_activ_rf', function(){
        $.get("users/rf_owned/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
  });   //Деактевировать RF

  $('body').on('click', '.change_activ_finger', function(){
        $.get("users/finger_owned/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
  });   //Деактевировать Finger



});

//Проверка состояния

window.setInterval(function(){
  if(index == "rfid_on" & turn > 0) {
    console.log(">>>");
    $.get("users/rfid_owned/", {cmd: 'add_check', user: $(".btn_active").attr("id") }, function(json) {
      console.log("g1");
      console.log(json);
      comand = JSON.parse(json);
      if (comand.cmd == "add") {
        turn = turn - 1;
      } else if (comand.cmd == "add_no") {
        console.log("g2>");
        $('#rfid_info').html(comand.data);
        index = "off"
        turn = 0;
      } else if (comand.cmd == "add_off") {
        console.log("no>");
        $.get("users/user_owned/", {cmd: 'user', user: $(".btn_active").attr("id") }, function(data) {
          console.log("g3>");
          $("#block_all_info").remove();
          $("#block_user_info").remove();
          $('#block_info').append(data);
          turn = 0;
          index = "off"
        });
      }
    });
  } else if (index == "finger_on" & turn > 0) {
    console.log("fin>");
    $.get("users/finger_owned/", {cmd: 'add_check', user: $(".btn_active").attr("id") }, function(json) {
      console.log("g1");
      console.log(json);
      comand = JSON.parse(json);
      if (comand.cmd == "add") {
        turn = turn - 1;
        if (comand.step != step) {
          console.log("step>");
          $('#finger_info').text(comand.data);
          if (comand.step == "exists" || comand.step == "not_match" || comand.step == "add") {
            step = "off"
            turn = 0;
          } else {
            turn = 14;
            step = comand.step;
          }
        }
      } else if (comand.cmd == "add_off") {
        console.log("no>");
        $.get("users/user_owned/", {cmd: 'user', user: $(".btn_active").attr("id") }, function(data) {
          console.log("g3>");
          $("#block_all_info").remove();
          $("#block_user_info").remove();
          $('#block_info').append(data);
          turn = 0;
          index = "off"
        });
      }
    });



  }
}, 1000);
