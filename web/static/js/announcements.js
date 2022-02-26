$(document).ready(() => {
    $('.timestamp').each((i, element) => {
        const epoch = $(element).html();
        const timestamp = new Date(Math.round(epoch) * 1000);
        const dateStr = `${timestamp.getDate()}/${timestamp.getMonth() + 1}/${timestamp.getFullYear()} ${timestamp.getHours()}:${timestamp.getMinutes()}`
        $(element).html(dateStr);
    }); 

    $.post('/api/announcements/read');
});