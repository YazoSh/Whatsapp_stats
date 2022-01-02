async function getAPI(url, callback) {
	fetch(url)
		.then(resp => resp.json())
		.then(data => callback(data)); //Replace with whatever
};

async function postAPI(url, file, callback) {
		formData = new FormData();
		formData.set('file', file, 'file');

		fetch(url, {
		  method: 'POST',
		  body: formData,
		})
		.then(resp => resp.json())
		.then(data => callback(data));
};
