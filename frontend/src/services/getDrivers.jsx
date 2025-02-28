export async function getDrivers(setDrivers, rankTitle) {
	await fetch(
		`/api/v1/main/drivers?rank_name=${rankTitle}`
	)
		.then(res => res.json())
		.then(data => {
			setDrivers(data);
		})
		.catch(err => console.error(err));
}
