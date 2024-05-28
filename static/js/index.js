$(document).ready(function(){
    $(function () {
        $('[data-bs-toggle="dropdown"]').dropdown();
    })
});
$(document).ready(function() {
    var isAuthenticated = $('#is-authenticated').val() === 'True';

    $('.save-button').click(function() {
        if (!isAuthenticated) {
            alert('Please log in to save videos.');
            window.location.href = '{{ url_for("web_routes.login") }}';
            return;
        }

        var videoId = $(this).data('video-id');
        var title = $(this).data('title');
        var thumbnail = $(this).data('thumbnail');

        $.ajax({
            url: '{{ url_for("web_routes.save_video") }}',
            type: 'POST',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': '{{ csrf_token() }}'  // Ensure you include CSRF token if using Flask-WTF
            },
            data: JSON.stringify({
                video_id: videoId,
                title: title,
                thumbnail: thumbnail
            }),
            success: function(data) {
                if (data.success) {
                    alert('Video saved successfully!');
                } else {
                    alert('Failed to save video.');
                }
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});
