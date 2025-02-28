export async function getRanks(setRanks) {
	await fetch("http://212.67.13.120:8000/api/v1/main/ranks")
		.then(res => res.json())
		.then(data => {
			setRanks(data);
		})
		.catch(err => console.error(err));
}
