function submitLoginDetails() {
    const username = $('#username-input').val();
    const password = $('#password-input').val();

    $.post('/api/login', {
        username,
        password
    }).done(() => {
        window.location = '/?banner=welcome'
    }).fail(() => {
        $('#username-input').addClass('is-invalid');
        $('#password-input').addClass('is-invalid');
        $('#login-invalid').slideDown();
    
        setTimeout(() => {
            $('#username-input').removeClass('is-invalid');
            $('#password-input').removeClass('is-invalid');
            $('#login-invalid').slideUp();
        }, 3000);
    });
}

$('#login-submit').click(() => {
    submitLoginDetails();
});

$("#username-input, #password-input").keydown((e) => {
    if (e.keyCode === 13) {
        submitLoginDetails();
    }
});
