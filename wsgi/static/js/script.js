local_fonts = ['DejaVu Sans Mono', 'Bitstream Vera Sans Mono',
    'Envy Code R', 'Liberation Mono'];

$("#font_select").change(function() {
    var font = $("#font_select").val();
    
    $("html").attr("class", "");
    $("pre").css("font-family", font);
    if (font == "monospace")
        return;
    
    var config = {};
    if ($.inArray(font, local_fonts) != -1) {
        config.custom = {
            families: [font],
            urls: ['/static/css/fonts.css']
        };
    } else {
        config.google = {
            families: [font]
        };
    }
    
    WebFont.load(config);
    
    update_permalink();
});

$("#size_select").change(function() {
    var size = $("#size_select").val();
    $("pre").css("font-size", size + "pt");
    update_permalink();
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
    var size = $("#size_select").val();
    var style = $("#style_select").val().toLowerCase();
    var theme = $("#theme_select").val().toLowerCase();
    
    var link = "/?font=" + font + "&size=" + size + "&style=" + style +
               "&theme=" + theme;
    $("#permalink").attr("href", link);
}

// google +1
(function() {
    var po = document.createElement('script');
    po.type = 'text/javascript';
    po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(po, s);
})();

$(document).ready(function() {
    $("#font_select").change();
    $("#size_select").change();
    update_permalink();
});
