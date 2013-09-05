$("#font_select").change(function() {
    var value = $("#font_select").val();
    $("pre").css("font-family", value);
    WebFont.load({
        google: {
            families: [value]
        }
    });
});

$("#theme_select").change(function() {
    var value = $("#theme_select").val().toLowerCase();
    var url = "//netdna.bootstrapcdn.com/bootswatch/3.0.0/" + value + "/bootstrap.min.css";
    
    $("#bootstrap_style").attr("href", url);
});
