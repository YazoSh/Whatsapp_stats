document.getElementById('gbutton').addEventListener('click', function(){
	path = document.getElementById('get-path').value;
	getAPI('http://localhost:8000/api' + path, function(data){
		console.log(data);
	});
});

document.getElementById('pbutton').addEventListener('click', function(){
	var file = document.getElementById('chatfile').files[0];

	postAPI('http://localhost:8000/api', file, function(data){
		console.log(data);
	});
});
