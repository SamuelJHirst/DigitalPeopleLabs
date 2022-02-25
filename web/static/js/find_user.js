function searchUsers() {
    const query = $('#user-search-query').val();

    $.get(`/api/user/search?query=${query}`, (response) => {
        if (response.length === 0) {
            
        }

        $('#main').html(`
            <div class="card" id="user-search-results">
                <h1 id="header">Search Results</h1>
                <ul class="list-group list-group-flush">
        `);

        for (const user of response) {
            let admin_badge = '';
            if (user.admin) {
                admin_badge = '<span class="badge bg-primary">Admin</span>';
            }

            $('#main').append(`
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

        $('#main').append(`
                </ul>
            </div>
        `);
    });
}

$('#name-button').click(() => {
    searchUsers();
});