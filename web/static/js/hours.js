$(document).ready(() => {
    $('.timestamp').each((i, element) => {
        const epoch = $(element).html();
        const timestamp = new Date(Math.round(epoch) * 1000);
        const dateStr = `${('0' + timestamp.getDate()).slice(-2)}/${('0' + (timestamp.getMonth() + 1)).slice(-2)}/${timestamp.getFullYear()} ${('0' + timestamp.getHours()).slice(-2)}:${('0' + timestamp.getMinutes()).slice(-2)}`
        $(element).html(dateStr);
    });
});

$('#shiftStart').click(() => {
    $.ajax('/api/hours/start', {
        contentType : 'application/json',
        method : 'POST',
        complete: () => {
            window.location = '/dashboard/hours';
        }
    });
});

$('#shiftEnd').click(() => {
    $.ajax('/api/hours/end', {
        contentType : 'application/json',
        method : 'POST',
        complete: () => {
            window.location = '/dashboard/hours';
        }
    });
});