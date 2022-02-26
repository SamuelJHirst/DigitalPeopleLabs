$('#announcementSubmit').click(() => {
    const title = $('#announcementTitle').val();
    const text = $('#announcementText').val();
    
    $.ajax('/api/admin/announcement', {
        data : JSON.stringify({
            title,
            text
        }),
        contentType : 'application/json',
        type : 'POST',
        complete: () => {
            window.location = '/dashboard/admin/announcements?name=' + title;
        }
    });
});