var index = "off";
var turn = 0;
var step = "off";
var modules = "not";
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
  $('body').on('click', '#add_rfid', function(){
    if ($('#add_rfid').text() == "Добавить") {
      console.log("1");
      $("#div_add_rfid").show();
      $("#div_add_rf").hide(); $('#add_rf').text("Добавить");
      $("#div_add_finger").hide(); $('#add_finger').text("Добавить");
      $('#add_rfid').text("Отмена");
      console.log("2");


      $.get("users/run_rfid/", {cmd: 'start', user: $(".btn_active").attr("id") }, function(data) {
        console.log("g1");
        console.log(data);
        $('#rfid_info').text(data);
      });

       console.log("3");
       turn = 14;
       modules = "rfid"

       console.log("end");
    } else if ($('#add_rfid').text() == "Отмена") {
      $("#div_add_rfid").hide();
      $('#add_rfid').text("Добавить");

      $.get("users/run_rfid/", {cmd: 'stop'}, function(data) {
        console.log("g1");
        console.log(data);
        $('#rfid_info').text(data);
      });
    }
    });   //Добавить RFID

  $('body').on('click', '#add_rf', function(){
    if ($('#add_rf').text() == "Добавить") {

      $("#div_add_rfid").hide(); $('#add_rfid').text("Добавить");
      $("#div_add_rf").show();
      $("#div_add_finger").hide(); $('#add_finger').text("Добавить");
      $('#add_rf').text("Отмена");

      $.get("users/run_rf/", {cmd: 'open', user: $(".btn_active").attr("id") }, function(data) {
        $('#rec_up_info').text("0000000000");
        $('#rec_down_info').text("0000000000");
      });

    } else if ($('#add_rf').text() == "Отмена") {
      $("#div_add_rf").hide();
      $('#add_rf').text("Добавить");
      $.get("users/run_rf/", {cmd: 'stop', user: $(".btn_active").attr("id") }, function(data) {
      });
    }
  });   //Добавить RF

  $('body').on('click', '#add_finger', function(){
    if ($('#add_finger').text() == "Добавить") {
      console.log("1");
      $("#div_add_rfid").hide(); $('#add_rfid').text("Добавить");
      $("#div_add_rf").hide(); $('#add_rf').text("Добавить");
      $("#div_add_finger").show();
      $('#add_finger').text("Отмена");

      $.get("users/finger_owned/", {cmd: 'add_start', user: $(".btn_active").attr("id") }, function(data) {
        console.log("g1");
        console.log(data);
        $('#finger_info').text(data);
      });

      console.log("3");
      turn = 14;
      index = "finger_on"

      console.log("end");

    } else if ($('#add_finger').text() == "Отмена") {
      $("#div_add_finger").hide();
      $('#add_finger').text("Добавить");
      turn = 0;
      index = "off"
      step = "off";
      $.get("users/finger_owned/", {cmd: 'add_cancel', user: $(".btn_active").attr("id") }, function(data) {
        $("#block_all_info").remove();
        $("#block_user_info").remove();
        $('#block_info').append(data);
      });
    }
  });   //Добавить Finger

  $('body').on('click', '#rec_up', function(){
    $.get("users/run_rf/", {cmd: 'up', user: $(".btn_active").attr("id") }, function(data) {
      console.log("g1");
      console.log(data);
      modules = "rf";
      turn = 15;
      $('#rec_info').text(data);
    });
  });   // Запись на открытие ворот

  $('body').on('click', '#rec_down', function(){
    $.get("users/run_rf/", {cmd: 'down', user: $(".btn_active").attr("id") }, function(data) {
      console.log("g1");
      console.log(data);
      modules = "rf";
      turn = 15;
      $('#rec_info').text(data);
    });
  });   // Запись на закрытие ворот


//Удалить
  $('body').on('click', '.delete_rfid', function(){
    if(confirm("Вы действительно хотите удалить?")) {
        $.get("users/run_rfid/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
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
      $.get("users/run_rfid/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
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
  if (modules == "rfid" || modules == "rf" || modules == "finger") {
    $.get("users/run_" + modules + "/", {cmd: 'check', user: $(".btn_active").attr("id") }, function(json) {
      console.log("g1");
      console.log(json);
      comand = JSON.parse(json);
      if (comand.cmd == "rec") {
        turn = turn - 1;
      } else if (comand.cmd == "no") {
        $('#' + modules + '_info').html(comand.data);
        modules = "off"
        turn = 0;
      } else if (comand.cmd == "save") {
        $.get("users/user_owned/", {cmd: 'user', user: $(this).attr("id") }, function(data) {
           $("#block_all_info").remove();
           $("#block_user_info").remove();
           $('#block_info').append(data);
        });
        modules = "off"
        turn = 0;
      } else if (comand.cmd == "time") {
        modules = "off"
        turn = 0;
        $("#div_add_" + modules).hide();
        $("#add_" + modules).text("Добавить");
      } else {
        console.log("xxxxxxxxxxxxxx");
      }
    });
  }
}, 1000);








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
      } else if (comand.cmd == "hz") {
        console.log("hz>>>>>>>>>>>>>>");
        console.log(comand.status);
        console.log(comand.step);
        console.log("hz>>>>>>>>>>>>>>>");
      }
    });



  } else if (index == "rf_on" & turn > 0) {
    console.log("rf_on");
    $.get("users/rf_owned/", {cmd: 'rec_check'}, function(json) {
      comand = JSON.parse(json);
      if (comand.cmd == "rec") {
        turn = turn - 1;

      } else if (comand.cmd == "rec_no") {
        $('#rf_info').text(comand.data);
        turn = 0;
      } else if (comand.cmd == "rec_up_yes") {
        $('#rec_info').text(comand.data);
        $('#rec_up_info').text(comand.code);
        turn = 0;
      } else if (comand.cmd == "rec_down_yes") {
        $('#rec_info').text(comand.data);
        $('#rec_down_info').text(comand.code);
        turn = 0;
      } else if (comand.cmd == "add_yes") {

      } else {
        turn = 0;
      }

    });
  }
}, 1000);
