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
        $('#existingUser').data('editing', response.username);
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
    const admin = $('#newUserAdminInput').is(':checked');

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
        $('#newUserEmailAddressInput').addClass('is-invalid');
        valid = false;
    }
    if (!jobTitle) {
        $('#newUserJobTitleInput').addClass('is-invalid');
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
        method : 'POST',
        complete: () => {
            window.location = '/dashboard/admin/users?name=' + firstName + ' ' + lastName + '&action=created';
        }
    });
});

$('#existingUserSubmit').click(() => {
    const oldUsername = $('#existingUser').data('editing');
    const firstName = $('#existingUserFirstNameInput').val();
    const lastName = $('#existingUserLastNameInput').val();
    const username = $('#existingUserUsernameInput').val();
    const password = $('#existingUserPasswordInput').val();
    const email = $('#existingUserEmailAddressInput').val();
    const jobTitle = $('#existingUserJobTitleInput').val();
    const admin = $('#existingUserAdminInput').is(':checked');

    let valid = true;

    if (!firstName) {
        $('#existingUserFirstNameInput').addClass('is-invalid');
        valid = false;
    }
    if (!lastName) {
        $('#existingUserLastNameInput').addClass('is-invalid');
        valid = false;
    }
    if (!username) {
        $('#existingUserUsernameInput').addClass('is-invalid');
        valid = false;
    }
    if (!email) {
        $('#existingUserEmailAddressInput').addClass('is-invalid');
        valid = false;
    }
    if (!jobTitle) {
        $('#existingUserJobTitleInput').addClass('is-invalid');
        valid = false;
    }

    if (!valid) {
        setTimeout(() => {
            $('#existingUserFirstNameInput').removeClass('is-invalid');
            $('#existingUserLastNameInput').removeClass('is-invalid');
            $('#existingUserUsernameInput').removeClass('is-invalid');
            $('#existingUserPasswordInput').removeClass('is-invalid');
            $('#existingUserEmailAddressInput').removeClass('is-invalid');
            $('#existingUserJobTitleInput').removeClass('is-invalid');
        }, 3000);
        return;
    }

    $.ajax('/api/admin/user', {
        data : JSON.stringify({
            oldUsername,
            firstName,
            lastName,
            username,
            password,
            email,
            jobTitle,
            admin
        }),
        contentType : 'application/json',
        method : 'PUT',
        complete: () => {
            window.location = '/dashboard/admin/users?name=' + firstName + ' ' + lastName + '&action=edited';
        }
    });
});