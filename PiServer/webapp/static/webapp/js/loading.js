$(window).on('load', function() {
  $(".loading-cover").css("opacity", "0");
  setTimeout(function() {
    $(".loading-cover").css('display', 'none');
  }, 400);
});
