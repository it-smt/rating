export async function getRanks(setRanks) {
	await fetch("http://localhost:8000/api/v1/main/ranks")
		.then(res => res.json())
		.then(data => {
			setRanks(data);
		})
		.catch(err => console.error(err));
}
