odoo.define('website_hotel_accommodation.accommodation', function (require) {
    "use strict";
    console.log('jhfds');
    var ajax=require('web.ajax');
    $("#add_guests").on('change', function() {
      if ($("#add_guests").is(':checked'))
         $("#table").show();
      else {
        $("#table").hide();
      }
    });
    $("#add_row").on('click', function() {
    var row = "<tr>"+
              "<td id='col0'>"+
              "<input type='text' name='name'/>"+
              "</td>"+
              "<td id='col2'>"+
              "<input type='number' name='age' value=''/>"+
              "</td></tr>";
    console.log($("#DyanmicTable tbody tr").length)
    $(table).find('tbody').append(row);
    console.log($("#DyanmicTable tbody tr").length,"after")
    });
});
