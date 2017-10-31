$(document).ready(function () {
    $('#join-list').submit(function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '',
            data: {
                csrfmiddlewaretoken: Cookies.get('csrftoken'),
                email: $('#email').val()
            },

            success: function () {
                $('#email').val('');
                document.getElementById('message').innerHTML =
                    'You are now in the mailing list, thank you for your interest!';
            },
            error: function () {
                document.getElementById('message').innerHTML =
                    'Sorry, we have encountered an error, maybe try again later?';
            }
        });
    });
});
