$(document).ready(function(){
  $(".mobile-nav").click(function(){
    $(".mobile-nav").toggleClass("mobile-nav-active");
    $(".mobile-content").toggleClass("mobile-content-active");
  });
});
