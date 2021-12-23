$(".pop_search").click(function (){
    val = $(this).text()
    var $myDD = $("#brand_search");
    $myDD.append("<option selected>"+ val +"</option>");

});

$('.next').click(function () {
    brand = $("#brand_search").val()
    var options = {};
    options.type = "GET";
    options.url = "ajax/get_categories_available/";
    options.type = "GET";
    options.data = {
        "brand": brand
    };
    options.dataType = "json";
    options.success = function (data) {
        if (data.length == 0) {
                $(".search_form").empty();
                $(".search_form").append("<h2>Sorry, we don't have any data on " + brand + " right now :( </h2>");
                $("#new_search").show();
                return
            }

            $(".popular_searches").empty();
            for (var i = 0; i < data.length; i++) {
            $("#available_categories").append("<option>" + data[i] + "</option>");
            $(".popular_searches").append('<button type="button" class="btn btn-dark btn-lg mt-2 pop_search">' + data[i] + '</button>')
        }
    }

    $.ajax(options);

    var current_fs, next_fs, previous_fs; //fieldsets
 
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    current_fs.hide();
    next_fs.show();
});