import "./Driver.scss";

export default function Driver({ driver, index }) {
	return (
		<div className="block-2__item">
			<div className="block-2__item-number">{index}</div>
			<div className="block-2__item-info">
				<div className="block-2__item-name">{driver.name}</div>
				<div className="block-2__item-delivery">Заказы: {driver.orders}</div>
			</div>
			<div className="block-2__item-other">{driver.callSign}</div>
		</div>
	);
}
