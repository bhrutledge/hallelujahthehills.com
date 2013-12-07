$(document).ready(function() {                              
    $("a[href$='jpg']").fancybox({
        'centerOnScroll': false,
        'overlayOpacity': .8,
        'overlayColor': '#000',
        'titleShow': false
    });

    $(".image-list a[href$='jpg']").fancybox({
        'centerOnScroll': false,
        'overlayOpacity': .8,
        'overlayColor': '#000',
        'titlePosition': 'inside'
    });

    $("#header-list-form label, #footer-contact-form label").inFieldLabels();
    $(".video a").embedly({'method': 'afterParent', 'maxWidth': 490});
    
    /*
    // TODO: Research jQuery lookup caching
    var jpContainer = $("#jp-container");
    var jpInterface = $("#jp-interface");
    var jpPlayTime = $("#jp-play-time");
    var jpTotalTime = $("#jp-total-time");
    
    $.jPlayer.defaults.swfPath = MEDIA_URL + "js";
    $.jPlayer.defaults.customCssIds = true;
    $.jPlayer.defaults.left = "-9999px";
    $.jPlayer.defaults.preload = 'metadata';
    $.jPlayer.timeFormat.padMin = false;

    jpContainer.jPlayer({
        ready: function() {
            loadSongCookie();
            
            $(".song .audio").click(function(event) {
                event.preventDefault();
                loadSong($(this), $(this).closest(".song").find('.title'));
                $(this).blur();
            });
            
            $("#article-header .audio").click(function(event) {
                event.preventDefault();
                loadSong($(this), $("#article-header h2"));
                $(this).blur();
            });
        }
    })
    .jPlayer("cssId", "play", "jp-play")
    .jPlayer("cssId", "pause", "jp-pause")
    .jPlayer("cssId", "stop", "jp-stop")
    .jPlayer("onProgressChange", function (loadPercent, playedPercentRelative, playedPercentAbsolute, playedTime, totalTime) {
        jpPlayTime.text($.jPlayer.convertTime(playedTime));
        jpTotalTime.text($.jPlayer.convertTime(totalTime));
    })
    .jPlayer("onSoundComplete", function() {
        jpContainer.jPlayer("stop");
    });

    function loadSongCookie() {            
        var diag = $.cookies.get("jp_diag");
        if (!diag) {
            return false;
        }
        
        $("#jp-song").html($.cookies.get("jp_song"));
        $("#jp-links").html($.cookies.get("jp_links"));
        
        jpContainer.jPlayer("setFile", diag.src)          
                   .jPlayer("playHeadTime", diag.playedTime);
        jpInterface.fadeIn();
        
        $.cookies.del("jp_diag");
        return true
    }

    function loadSong(audio, title) {
        var audioPath = audio.attr("href");
        if (!audioPath) {
            return false;
        }
        
        var detailsPath = title.attr("href");
        if (!detailsPath) {
            detailsPath = window.location.pathname;
        }

        $("#jp-song").text(title.text());
        $("#jp-details").attr("href", detailsPath);
        $("#jp-download").attr("href", audioPath);

        jpContainer.jPlayer("setFile", audioPath)
                   .jPlayer("play");
        jpInterface.fadeIn();
        
        return true;
    }

    $(window).unload(function() {
        var config = jpContainer.data("jPlayer.config");
        if (!config.diag.isPlaying) {
            return;
        }

        jpContainer.jPlayer("pause");
        
        var expireTime = new Date().getTime();
        expireTime = expireTime + 60000; // 1 minute

        $.cookies.set("jp_diag", config.diag, {'expiresAt': new Date(expireTime)});
        $.cookies.set("jp_song", $("#jp-song").html());
        $.cookies.set("jp_links", $("#jp-links").html());
    });
    */
});
