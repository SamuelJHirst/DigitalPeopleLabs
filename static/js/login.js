$('#login-submit').click(() => {
    $('#username-input').addClass('is-invalid');
    $('#password-input').addClass('is-invalid');
    $('#login-invalid').slideDown();

    setTimeout(() => {
        $('#username-input').removeClass('is-invalid');
        $('#password-input').removeClass('is-invalid');
        $('#login-invalid').slideUp();
    }, 3000);
});