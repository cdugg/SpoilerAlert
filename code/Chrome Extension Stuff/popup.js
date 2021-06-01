//interaction with the popup page
'use strict';

document.addEventListener('DOMContentLoaded', function () {
  var button = document.getElementById('searchbut');
  button.onclick = addMovie;
});

function addMovie(){
	var x = document.getElementById("search");
	if (x.value != ""){
		//TODO html get from imdb get movie name from link and characters names contained in cast div
		//TODO set x.value to movie name
		//TODO add characters to some kind of active/inactive dictionary
		var link = x.value;
		//https://www.imdb.com/title/tt4154796/
		console.log(link);


		var movies = document.getElementById("movies");

		//check if the movie is already in the extension list so no duplicates
		var i = 0;
		var yn = true
		while (i < movies.children["length"]){
			if (movies.children[i].id == x.value){
				yn = false
			}
			i++;
		}
		
		//if movie isnt already in list add and give event listeners
		if (yn == true){
			movies.insertAdjacentHTML('beforeend', "<div id=\"" + x.value + "\"><p id = \"p\">" + x.value + "</p><label class=\"switch\"><input type=\"checkbox\" checked><span class=\"slider round\"></span></label><button type=\"submit\" id=\"" + x.value + "del\"><img id=\"" + x.value + "img" + "\"src=\"images/trash.png\"></button></div>");
			var delet = x.value + "del";
			var delmov = document.getElementById(delet)
			delmov.addEventListener('click', delMovie);
			x.value = "";
			//TODO add on off switch event listener
		}
	}
}

function delMovie(event){
	var divid = event.target.id
	divid = divid.substring(0, divid.length - 3);
	var elem = document.getElementById(divid);
    elem.parentNode.removeChild(elem);
}

//TODO switch event handler
function activate(event){
	console.log('activate switch');
}

