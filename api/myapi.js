async function getAPI(url, callback) {
	fetch(url)
		.then(resp => resp.json())
		.then(data => callback(data)); //Replace with whatever
};

async function postAPI(url, data, callback) {
		fetch(url, {
		  method: 'POST',
		  headers: {
			'Content-Type': 'text/plain',
			'Content-Length': data.length,
		  },
		  body: data,
		})
		.then(resp => resp.json())
		.then(data => callback(data));
};
