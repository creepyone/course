$(document).ready(function() {

    $('.dropdown-toggle').dropdown();

    $('#filter').click(
        function(){
            dynamic_queries();
        }
    );

    function dynamic_queries(){
        var message = {
                genre: $('#genre').val()
            }
        $('#result_table').empty();
        $.ajax({
            type:'POST',
            url: '/get_genre',
            processData: false,  // tell jQuery not to process the data
            contentType: false,  // tell jQuery not to set contentType
            data: JSON.stringify(message),
            success: (data) => {
                    console.log(data);
                    for(i in data)
                    {
                        movie = data[i]
                        $('#result_table').append("<tr>" +
                        "<td>"+movie['film_id']+"</td>" +
                        "<td>"+movie['title']+"</td>" +
                        "<td>"+movie['year']+"</td>" +
                        "<td>"+movie['genre']+"</td>" +
                        "<td>"+movie['votes']+"</td>" +
                        "</tr>")
                    }

                }
            });
    }
});
