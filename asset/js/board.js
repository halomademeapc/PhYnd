$(document).ready(function() {
    $(".boarditem").each(function() {
        if ($.trim($(this).text()) == 'O') {
            $(this).html('<i class="far fa-circle"></i>');
            $(this).addClass('naughts');
        } else if ($.trim($(this).text()) == 'X') {
            $(this).html('<i class="fas fa-times"></i>');
            $(this).addClass('crosses');
        } else {
            $(this).html('');
            $(this).addClass('unclaimed');
        }
    });
});