$("#font_select").change(function() {
    var value = $("#font_select").val();
    
    $("html").attr("class", "");
    $("pre").css("font-family", value);
    if (value == "Monospace")
        return;
    
    WebFont.load({
        google: {
            families: [value]
        }
    });
});

$("#style_select").change(function() {
    var style = $("#style_select").val().toLowerCase();
    var url = "/style/" + style;
    $("#source_style").attr("href", url);
});

$("#theme_select").change(function() {
    var value = $("#theme_select").val().toLowerCase();
    var url = "//netdna.bootstrapcdn.com/bootswatch/3.0.0/" + value + "/bootstrap.min.css";
    
    $("#bootstrap_style").attr("href", url);
});
