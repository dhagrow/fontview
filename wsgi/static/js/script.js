$("#font_select").change(function() {
    var font = $("#font_select").val();
    
    $("html").attr("class", "");
    $("pre").css("font-family", font);
    if (font == "Monospace")
        return;
    
    WebFont.load({
        google: {
            families: [font]
        }
    });
    
    update_permalink()
});

$("#style_select").change(function() {
    var style = $("#style_select").val().toLowerCase();
    var url = "/style/" + style;
    $("#source_style").attr("href", url);
    
    update_permalink()
});

$("#theme_select").change(function() {
    var theme = $("#theme_select").val().toLowerCase();
    var url = "//netdna.bootstrapcdn.com/bootswatch/3.0.0/" + theme + "/bootstrap.min.css";
    
    $("#bootstrap_style").attr("href", url);
    
    update_permalink()
});

function update_permalink() {
    var font = $("#font_select").val().replace(/\s*/g, "").toLowerCase();
    var style = $("#style_select").val().toLowerCase();
    var theme = $("#theme_select").val().toLowerCase();
    
    var link = "/?font=" + font + "&style=" + style + "&theme=" + theme;
    $("#permalink").attr("href", link);
}

$(document).ready(function() {
    update_permalink();
});
