/*
 * Main functions
 *
 */
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

//Function to requeset and clean up all the Projects from server
function getProjects(callback){
 $.ajax({
  type: "GET",
  url: "/_get_all_projects/",
  success: function(res){
    if (res){
      res = JSON.parse(res);
      //Parse through every key in response and fix server formatting
      for (var key in res){
        var curPriority = res[key];
        for (var projKey in curPriority){
          var parsedProject = JSON.parse(curPriority[projKey])[0];
          curPriority[projKey] = parsedProject["fields"];
          curPriority[projKey]["id"] = parsedProject["pk"];
        }
      }
      if (callback){
        callback(res);
      }else{
        return res;
      }
    }else{
      console.log("Project response from server incorrect");
    }
  }
 });
}

//Loads Projects onto the portfolio section
function loadProjects(projects, callback){
  var numProjects = 4;
  var sortedPriorities = sortPriority(projects);
  for (var i in sortedPriorities){
    var curProjects = projects[sortedPriorities[i]];
    for (var j in curProjects){
      var project = curProjects[j];
      if (numProjects == 0){
        if (callback){
          callback();
        }else{
          return true;
        }
      }else{
        if (numProjects < 3){
          createProjectDiv(project, "row-2"); 
        }else{
          createProjectDiv(project, "row-1");
        }
        numProjects--;
      }
    }
  }
}

/*
 * Helper Functions
 */

//Function to return an array of sorted priorities
function sortPriority(projects){
  var priorityArray = [];
  for (var key in projects){
    priorityArray.push(key);
  }
  return priorityArray.sort(function(a,b){
    return b - a;
  });
}

//Function to load project-containers with project information
function createProjectDiv(project, parentID){
  var id = project.id;
  var name = project.project_name;
  var date = project.strDate;
  var projImg = project.project_url;
  $("#" + parentID).append("<div class = project-container id = project-" + id + "><div class = project-meta><div class = project-name>" + name + "</div><div class = project-date>" + date + "</div></div></div>");
  $("#project-" + id).css({"background-image": "url(" + projImg +")"});
}

//Event Catchers
$(window).load(function(){
  adjustProject();
});

$(window).resize(function(){
  adjustProject();
});

//Main
$(document).ready(function(){
  //Get Projects
  getProjects(function(projects){
    loadProjects(projects, function(){
      adjustProject();
    });
  });
});
