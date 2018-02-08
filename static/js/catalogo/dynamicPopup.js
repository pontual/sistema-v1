$(document).on("pagecreate", "#produtos-page", function() {
  var drift;
  $(".produtos").on("click", function() {
    var target = $(this);
    var short = target.attr("id");
    var closebtn = '<a href="#" data-rel="back" class="ui-btn ui-corner-all ui-btn-a ui-icon-delete ui-btn-icon-notext ui-btn-right">Fechar</a>';
    // var header = '<div data-role="header"><h2>' + short.substring(5) + '</h2></div>';
    var header = '<div data-role="header"><h2>Toque para ampliar</h2></div>';

    var img = '<img src="/fotos/' + short + '.jpg" data-zoom="/fotos/' + short + '.jpg" id="img-' + short + '" alt="foto" class="photo">';
    var popup = '<div data-role="popup" id="popup-' + short + '" data-short="' + short + '" data-theme="none" data-overlay-theme="a" data-corners="false" data-tolerance="15"></div>';

    $(header).appendTo($(popup)
                       .appendTo($.mobile.activePage)
                       .popup())
      .toolbar()
      .before(closebtn)
      .after(img);

    // Show spinner
    $.mobile.loading("show", {
      text: "",
      textVisible: false,
      theme: $(this).jqmData("theme"),
      textonly: false,
      html: ""
    });
    

    $(".photo", "#popup-" + short).load(function() {
      $("#popup-" + short).popup("open");
      
      drift = new Drift($("#img-" + short).get(0), {
        containInline: false,
        inlinePane: true,
        inlineOffsetY: -90,
        zoomFactor: 3,
      });

      clearTimeout(fallback);

      // clear spinner
      $.mobile.loading("hide");
    });

    var fallback = setTimeout(function() {
      $("#popup-" + short).popup("open");

      // clear spinner
      $.mobile.loading("hide");
    }, 5000);
  });

  // Set a max-height
  $(document).on("popupbeforeposition", ".ui-popup", function() {
    var image = $(this).children("img"),
    height = image.height(),
    width = image.width();
    $(this).attr({ "height": height, "width": width });
    var maxHeight = $(window).height() - 68 + "px";
    $("img.photo", this).css("max-height", maxHeight);
  });

  $(document).on("popupafterclose", ".ui-popup", function() {
    drift.zoomPane._completeHide();
    $(this).remove();
  });
});
