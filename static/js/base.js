$(document).ready(function () {
    $('#hamburger').on('click', function (event) {
        document.getElementById('hamburger').classList.toggle('cross');
        document.getElementById('menu').classList.toggle('expose');
        document.getElementById('content').classList.toggle('shimmy');
        event.stopPropagation();
    });

    $('#content').on('click', function (event) {
        $('#hamburger').removeClass('cross');
        $('#menu').removeClass('expose');
        $('#content').removeClass('shimmy');
        event.stopPropagation();
    })
});
