if (typeof jQuery === "undefined") {
    console.log("Erro: jQuery necessário!");
}

var theme = document.createElement('link');
theme.rel = 'stylesheet';
theme.type = 'text/css';
theme.href = 'http://127.0.0.1:5001/static/cdn/css/libnotify.css';
document.getElementsByTagName('head')[0].appendChild(theme);

var humane = document.createElement("script");
humane.type = 'text/javascript';
humane.src = "http://127.0.0.1:5001/static/cdn/js/humane.js";
document.getElementsByTagName("body")[0].appendChild(humane);

var gamify = (function () {
    var object = {};
    var url = "http://127.0.0.1:5001/api";

    object.track = function (properties) {
        $.ajax({
            url: url + "/track",
            jsonp: "callback",
            dataType: "jsonp",
            data: properties,
            success: function (response) {
                console.log(response);
                eval(response.script);
            }
        });
    };

    return object;
})();