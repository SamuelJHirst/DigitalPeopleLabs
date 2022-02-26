function searchUsers() {
    const query = $('#user-search-query').val();

    $.get(`/api/user/search?query=${query}`, (response) => {
        if (response.length === 0) {
            $('#search-results').html(`
                <div class="card mb-3">
                    <div class="card-body">
                        <span><em>No results found.</em></span>
                    </div>
                </div>
            `);
            return;
        }

        $('#search-results').html(`
            <div class="card" id="user-search-results">
                <ul class="list-group list-group-flush">
        `);

        for (const user of response) {
            let admin_badge = '';
            if (user.admin) {
                admin_badge = '<span class="badge bg-primary">Admin</span>';
            }

            $('#search-results').append(`
                <li class="list-group-item">
                    <div class="row">
                        <div class="col-1">
                            <img src="/static/img/login.png" class="user-img" />
                        </div>
                        <div class="col">
                            <h6>${user.first_name} ${user.last_name}   ${admin_badge}</h6>
                            <span>${user.job_title}</span>
                        </div>
                    </div>
                </li>
            `);
        }

        $('#search-results').append(`
                </ul>
            </div>
        `);
    });
}

$('#name-button').click(() => {
    searchUsers();
});

$("#user-search-query").keydown((e) => {
    if (e.keyCode === 13) {
        searchUsers();
    }
});