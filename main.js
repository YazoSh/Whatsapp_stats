document.getElementById('gbutton').addEventListener('click', function(){
	path = document.getElementById('get-path').value;
	getAPI('http://localhost:8000/' + path, function(data){
		console.log(data);
	});
});

document.getElementById('pbutton').addEventListener('click', function(){
	var blob = document.getElementById('chatfile').files[0];

	blob.text().then(text => postAPI('http://localhost:8000/', text, function(text){
		console.log(text);
	}));
});
