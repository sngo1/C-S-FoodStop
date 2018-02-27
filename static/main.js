/*
  csFoodStop
  Samantha Ngo and Carol Pan
  SoftDev2 pd7
  K06 -- Ay Mon, Go Git it From Yer Flask
  2018-02-27
*/

var state_form = document.getElementById("state")
var display = document.getElementById("info")
var button = document.getElementById("submit")
var reps = []

var getNames = function(){
    console.log("test")
    display.innerHTML = ""
    $.ajax({
	url: "/find",
	type: "GET",
	data: {state: state_form.value},
	success: function(d){
	    reps=JSON.parse(d);
	    listRep();
	}
    });
}

var listRep = function(){
    var i;
    for (i=0; i<reps.length; i++){
	li = document.createElement("li");
	li.innerHTML = reps[i];
	display.appendChild(li)
    };
}

submit.addEventListener('click',getNames)
