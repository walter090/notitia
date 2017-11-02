$(document).ready(function () {
    $('#hamburger').on('click', function (event) {
        document.getElementById('hamburger').classList.toggle('cross');
        document.getElementById('menu').classList.toggle('expose');
        document.getElementById('content').classList.toggle('shimmy');
        document.getElementById('content').classList.toggle('diable_all');
        event.stopPropagation();
    });

    $('#content').on('click', function (event) {
        $('#hamburger').removeClass('cross');
        $('#menu').removeClass('expose');
        $('#content').removeClass('shimmy');
        $('#content').removeClass('disable_all');
        event.stopPropagation();
    })
});
