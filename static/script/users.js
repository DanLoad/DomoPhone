var modules = "no";
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
       modules = "rfid";

       console.log("end");
    } else if ($('#add_rfid').text() == "Отмена") {
      $("#div_add_rfid").hide();
      $('#add_rfid').text("Добавить");
      modules = "off"
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
        modules = "rf"
      });

    } else if ($('#add_rf').text() == "Отмена") {
      $("#div_add_rf").hide();
      $('#add_rf').text("Добавить");
      modules = "off";
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

      $.get("users/run_finger/", {cmd: 'start', user: $(".btn_active").attr("id") }, function(data) {
        console.log("g1");
        console.log(data);
        $('#finger_info').text(data);
      });

      console.log("3");
      modules = "finger";

      console.log("end");

    } else if ($('#add_finger').text() == "Отмена") {
      $("#div_add_finger").hide();
      $('#add_finger').text("Добавить");
      modules = "off";
      $.get("users/run_finger/", {cmd: 'stop', user: $(".btn_active").attr("id") }, function(data) {
        console.log(data);
      });
    }
  });   //Добавить Finger

  $('body').on('click', '#rec_up', function(){
    $.get("users/run_rf/", {cmd: 'up', user: $(".btn_active").attr("id") }, function(data) {
      console.log("g1");
      console.log(data);
      modules = "rf";
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

  $('body').on('click', '#save_rf', function(){
    $.get("users/run_rf/", {cmd: 'save'}, function(data) {
      console.log("g1");
      console.log(data);
      modules = "rf";
      $('#rec_info').text(data);
    });
  });   // Сохранить брелок

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
        $.get("users/run_rf/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
    }
  });   //Удалить RF

  $('body').on('click', '.delete_finger', function(){
    if(confirm("Вы действительно хотите удалить?")) {
        $.get("users/run_finger/", {cmd: 'delete', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
         modules = "finger";
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
        $.get("users/run_rf/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
  });   //Деактевировать RF

  $('body').on('click', '.change_activ_finger', function(){
        $.get("users/run_finger/", {cmd: 'activ', index: $(this).attr("id"), user: $(".btn_active").attr("id") }, function(data) {
         $("#block_all_info").remove();
         $("#block_user_info").remove();
         $('#block_info').append(data);
       });
  });   //Деактевировать Finger



});

//Проверка состояния

window.setInterval(function(){
  if (modules != "no") {
    if (modules == "rfid" || modules == "rf" || modules == "finger") {
      $.get("users/run_" + modules + "/", {cmd: 'check', user: $(".btn_active").attr("id") }, function(json) {
        console.log("g1");
        console.log(json);
        comand = JSON.parse(json);
        if (comand.cmd == "rec") {
          if (modules == "finger") {
            if (comand.step == "wait") {
              $('#finger_info').text("Подождите");
            } else if (comand.step == "one") {
              $('#finger_info').text("Прикладите палец на сенсор");
            } else if (comand.step == "remove") {
              $('#finger_info').text("Уберите палец");
            } else if (comand.step == "two") {
              $('#finger_info').text("Прикладите палец на сенсор снова");
            }
          }
        } else if (comand.cmd == "up" || comand.cmd == "down") {
        } else if (comand.cmd == "ok_up") {
          $('#rec_up_info').text(comand.data);
          modules = "no"
        } else if (comand.cmd == "ok_down") {
          $('#rec_down_info').text(comand.data);
          modules = "no"
        } else if (comand.cmd == "start") {
          $('#' + modules + '_info').text(comand.data);
        } else if (comand.cmd == "no") {
          if (modules == "finger") {
            if (comand.step == "error") {
              $('#finger_info').text("Ошибка");
            } else if (comand.step == "exists") {
              $('#' + modules + '_info').html(comand.data);
            } else if (comand.step == "not_match") {
              $('#finger_info').text("Пальци не совпадают");
            } else if (comand.step == "full") {
              $('#finger_info').text("База заполнена");
            } else {
              $('#' + modules + '_info').html(comand.data);
            }
          } else if (modules == "rfid") {
            $('#rfid_info').html(comand.data);
          } else if (modules == "rf") {
            $('#rec_info').html(comand.data);
          }
          modules = "no"
        } else if (comand.cmd == "delete" & comand.step == "delete") {
        } else if (comand.cmd == "save" || comand.cmd == "delete" & comand.step == "ok") {
          $.get("users/user_owned/", {cmd: 'user', user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
          });
          modules = "no"
        } else if (comand.cmd == "wait") {
        } else if (comand.cmd == "time") {
          modules = "no"
          $.get("users/user_owned/", {cmd: 'user', user: $(".btn_active").attr("id") }, function(data) {
             $("#block_all_info").remove();
             $("#block_user_info").remove();
             $('#block_info').append(data);
          });
        } else {
          console.log("xxxxxxxxxxxxxx");
          modules = "off"
        }
      });
    }
  }
}, 1000);
