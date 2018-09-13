/**
 * Created with IntelliJ IDEA.
 * User: eperreau
 * Date: 13/09/13
 * Time: 14:42
 * To change this template use File | Settings | File Templates.
 */


jQuery(document).ready(function($) {

  var digitalAristotle=0

  if(digitalAristotle==0){
    digitalAristotle=1;
    $('#conversation').animate({scrollTop: $('#conversation').prop("scrollHeight")},
            $('#conversation').height());
  }

  $('.clearconversation').click(function(e){
    e.preventDefault();
  });


  $('#elizaibotform').submit(function(e) {
    e.preventDefault();
    if (user == "") {
      return;
    }

    $('#conversation').animate({scrollTop: $('#conversation').prop("scrollHeight")},
            $('#conversation').height());
    formdata = $("#elizaibotform").serialize();
    $('#elizaibotsay').val('')
    $('#elizaibotsay').focus();

    $.post(baseurl+'lib/chat.php', formdata, function(returnData) {
      var botsaid = "";
      botsaid = returnData;
      $('#conversation').append("<div class='response'>" +
                                "<div class='botsay'><span class='whosay'>Bot:</span>" +
                                "<span class='sayit'>" + botsaid + "</span></div></div>");
      $('#conversation').animate({scrollTop: $('#conversation').prop("scrollHeight")},
              $('#conversation').height());


      $('#conversation').animate({scrollTop: $('#conversation').prop("scrollHeight")},
            $('#conversation').height());

      return false;
     });
  });
});
