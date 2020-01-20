    var ws = new WebSocket("ws://localhost:8000");
    // Close socket when window closes
    $(window).on('beforeunload', function(){
       ws.close();
    });
    ws.onerror = function(event) {
        location.reload();
    }
    ws.onmessage = function(event)  {
        var message_received = event.data;
        chat_add_message(message_received, false);
    };
    // Add a message to the chat history
    function chat_add_message(message, isUser) {
        var class_suffix = isUser ? '_user' : '';
        var html = '\
        <div class="chat_line">\
            <div class="chat_bubble'+class_suffix+'">\
              <div class="chat_triangle'+class_suffix+'"></div>\
                '+message+'\
            </div>\
        </div>\
        ';
        chat_add_html(html);
    }
    // Add HTML to the chat history
    function chat_add_html(html) {
        $("#chat_log").append(html);
        chat_scrolldown();
    }
    // Scrolls the chat history to the bottom
    function chat_scrolldown() {
        $("#chat_log").animate({ scrollTop: $("#chat_log")[0].scrollHeight }, 500);
    }
    // If press ENTER, talk to chat and send message to server
    $(function() {
       $('#chat_input').on('keypress', function(event) {
          if (event.which === 13 && $(this).val() != ""){
             var message = $(this).val();
             $(this).val("");
             chat_add_message(message, true);
             ws.send(message);
          }
       });
    });
        function myFunction() {
      ws.send("click");
    }
    function check(e) {
      var x = e.keyCode;

	  if (x == 40){      // handling up arrow key
		if (s_g == -2){
			s_g = store.length -1;
		}
		document.getElementById("chat_input").value = store[s_g];
		if (s_g != (store.length -1)){
            s_g = s_g + 1;
		}

		}
	  else if (x == 38){     // handling down arrow key
		if (s_g == -2){
			s_g = store.length -1;
		}
		document.getElementById("chat_input").value = store[s_g];
		if (s_g != 0){
            s_g = s_g -1;
		}

        }

    }