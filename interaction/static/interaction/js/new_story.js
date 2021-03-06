// Expandable textarea
// Modified from https://stackoverflow.com/questions/454202/creating-a-textarea-with-auto-resize
var observe;
if (window.attachEvent) {
    observe = function (element, event, handler) {
        element.attachEvent('on' + event, handler);
    };
}
else {
    observe = function (element, event, handler) {
        element.addEventListener(event, handler, false);
    };
}
$(document).ready(function () {
    var element = document.getElementsByClassName('story');
    [].forEach.call(element, function (text) {
        function resize() {
            text.style.height = 'auto';
            text.style.height = text.scrollHeight + 'px';
        }

        function delayedResize() {
            window.setTimeout(resize, 0);
        }

        observe(text, 'change', resize);
        observe(text, 'cut', delayedResize);
        observe(text, 'paste', delayedResize);
        observe(text, 'drop', delayedResize);
        observe(text, 'keydown', delayedResize);
    });

    $('#publish_button').on('click', function (event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '',
            data: {
                csrfmiddlewaretoken: Cookies.get('csrftoken'),
                title: $('#title').html(),
                subtitle: $('#subtitle').html(),
                tldr: $('#tldr').html(),
                content_body: $('#content_body').html()
            },
            success: function (response) {
                // Redirect to url sent by server
                if(response.all_clear){
                    window.location.replace(response.url);
                } else {
                    document.getElementById('error_messages').innerHTML = response.messages;
                }
            }
        });
    });
});
