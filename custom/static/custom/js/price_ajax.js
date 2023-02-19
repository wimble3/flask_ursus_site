$( document).ready(function() {
    $('select').change(function() {
        $.ajax({
            url: '/custom/ajax',
            type: 'get',
            dataType: 'json',
            data: {
                length: $('#length').val(),
                blade_material: $('#blade_material').val(),
                blade_length: $('#blade_length').val(),
                blade_thickness: $('#blade_thickness').val(),
                handle_material: $('#handle_material').val(),
                coating: $('#coating').val(),
            },
            success (data) {
                total_price_text = 'Total price: ' + data['total_price'] + '$'
                $('.response h2').text(total_price_text);
                $('#total_price').remove();
                $('.response').append('<input name="total_price" id="total_price" type="text" value="' + data['total_price'] + '"hidden>');
            },
            error: function () {
                alert('Sorry, something wrong!');
            },
        });
    });
});
