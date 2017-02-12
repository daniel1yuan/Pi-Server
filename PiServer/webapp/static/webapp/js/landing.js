//Function to Adjust scale of Project divs
function adjustProject(){
  var projectHeight = $(".project-grid-row").height() - 20;
  var projectWidth = .5*$(".project-grid-row").width() - 20;
  if (projectWidth > projectHeight){
    $(".project-container").width(projectHeight);
    $(".project-container").height(projectHeight);
  }else{
    $(".project-container").width(projectWidth);
    $(".project-container").height(projectWidth);
  }
}

//Event Catchers
$(window).load(function(){
  adjustProject();
});

$(window).resize(function(){
  adjustProject();
});
