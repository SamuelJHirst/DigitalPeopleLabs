$('#newLinkSubmit').click(() => {
    const linkName = $('#newLinkName').val();
    const linkTextColour = $('#newLinkTextColour').val();
    const linkBackgroundColour = $('#newLinkBackgroundColour').val();
    const linkURL = $('#newLinkURL').val();

    $.ajax('/api/admin/links', {
        data: JSON.stringify({
            "name": linkName,
            "textColour": linkTextColour,
            "backgroundColour": linkBackgroundColour,
            "url": linkURL
        }),
        contentType: 'application/json',
        method: 'POST',
        complete: () => {
            window.location = '/dashboard/admin/links'
        }
    })
});