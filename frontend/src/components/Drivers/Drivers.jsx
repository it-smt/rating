import { useContext, useEffect } from "react";
import { DriversContext } from "../../providers/DriversProvider";
import { RankTitleContext } from "../../providers/RankTitleProvider";
import { getDrivers } from "../../services/getDrivers";
import Driver from "./Driver/Driver";
import "./Drivers.scss";

export default function Drivers() {
	let index = 1;
	const { drivers, setDrivers } = useContext(DriversContext);
	const { rankTitle } = useContext(RankTitleContext);

	useEffect(() => {
		getDrivers(setDrivers, rankTitle);
	}, [rankTitle]);

	const renderDrivers = (grade, title, className) => (
		<div className={`block-2__${className}`}>
			<div className={`block-2__title ${className}`}>{title}</div>
			{drivers
				.filter(driver => driver.grade === grade)
				.map(driver => {
					return (
						<Driver key={driver.id} driver={{ ...driver }} index={index++} />
					);
				})}
		</div>
	);

	return (
		<div className="block-2">
			{renderDrivers("up", "Места на повышение", "places-upgrade")}
			{renderDrivers("remain", "Места без изменений", "places")}
			{renderDrivers("down", "Места на понижение", "places-downgrade")}
		</div>
	);
}
