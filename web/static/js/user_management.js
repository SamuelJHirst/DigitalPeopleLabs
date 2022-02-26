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