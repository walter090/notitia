$(document).ready(function () {
    $('#hamburger').on('click', function (event) {
        document.getElementById('hamburger').classList.toggle('cross');
        document.getElementById('menu').classList.toggle('expose');
        document.getElementById('content').classList.toggle('shimmy');
        document.getElementById('content').classList.toggle('disable_all');
        $('#quick_login').attr('disabled', '');
        event.stopPropagation();
    });

    $('#content').on('click', function (event) {
        var content = $('#content');
        $('#hamburger').removeClass('cross');
        $('#menu').removeClass('expose');
        content.removeClass('shimmy');
        content.removeClass('disable_all');
        $('#quick_login').removeAttr('disabled');
        event.stopPropagation();
    })
});
