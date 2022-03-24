$('#new-user-tab').click(() => {
    setTimeout(() => {
        $('#user-search-query').val('');
        $('#existingUserFirstNameInput').val('');
        $('#existingUserLastNameInput').val('');
        $('#existingUserEmailAddressInput').val('');
        $('#existingUserJobTitleInput').val('');
        $('#existingUserUsernameInput').val('');
        $('#existingUserAdminInput').attr('checked', false);
        $('#existingUser').hide();
    }, 500);
});

function getUser() {
    const query = $('#user-search-query').val();

    $.get(`/api/user/get?query=${query}`, (response) => {
        $('#existingUserFirstNameInput').val(response.first_name);
        $('#existingUserLastNameInput').val(response.last_name);
        $('#existingUserEmailAddressInput').val(response.email_address);
        $('#existingUserJobTitleInput').val(response.job_title);
        $('#existingUserUsernameInput').val(response.username);
        $('#existingUserAdminInput').attr('checked', response.admin);
        $('#existingUser').slideDown();
    });
}

$('#name-button').click(() => {
    getUser();
});

$("#user-search-query").keydown((e) => {
    if (e.keyCode === 13) {
        getUser();
    }
});

$('#newUserSubmit').click(() => {
    const firstName = $('#newUserFirstNameInput').val();
    const lastName = $('#newUserLastNameInput').val();
    const username = $('#newUserUsernameInput').val();
    const password = $('#newUserPasswordInput').val();
    const email = $('#newUserEmailAddressInput').val();
    const jobTitle = $('#newUserJobTitleInput').val();
    const admin = $('#newUserAdmin').is(':checked');

    let valid = true;

    if (!firstName) {
        $('#newUserFirstNameInput').addClass('is-invalid');
        valid = false;
    }
    if (!lastName) {
        $('#newUserLastNameInput').addClass('is-invalid');
        valid = false;
    }
    if (!username) {
        $('#newUserUsernameInput').addClass('is-invalid');
        valid = false;
    }
    if (!password) {
        $('#newUserPasswordInput').addClass('is-invalid');
        valid = false;
    }
    if (!email) {
        $('#newUserJobTitleInput').addClass('is-invalid');
        valid = false;
    }
    if (!jobTitle) {
        $('#newUserEmailAddressInput').addClass('is-invalid');
        valid = false;
    }

    if (!valid) {
        setTimeout(() => {
            $('#newUserFirstNameInput').removeClass('is-invalid');
            $('#newUserLastNameInput').removeClass('is-invalid');
            $('#newUserUsernameInput').removeClass('is-invalid');
            $('#newUserPasswordInput').removeClass('is-invalid');
            $('#newUserEmailAddressInput').removeClass('is-invalid');
            $('#newUserJobTitleInput').removeClass('is-invalid');
        }, 3000);
        return;
    }

    $.ajax('/api/admin/user', {
        data : JSON.stringify({
            firstName,
            lastName,
            username,
            password,
            email,
            jobTitle,
            admin
        }),
        contentType : 'application/json',
        type : 'POST',
        complete: () => {
            window.location = '/dashboard/admin/users?name=' + firstName + ' ' + lastName;
        }
    });
});