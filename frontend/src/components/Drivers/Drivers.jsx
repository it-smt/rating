import { driversData } from "../../assets/drivers";
import Driver from "./Driver/Driver";
import "./Drivers.scss";

export default function Drivers() {
	let index = 1;

	const renderDrivers = (type, title, className) => (
		<div className={`block-2__${className}`}>
			<div className={`block-2__title ${className}`}>{title}</div>
			{driversData
				.filter(driver => driver.type === type)
				.map((driver, i) => {
					return <Driver key={i} driver={{ ...driver }} index={index++} />;
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
