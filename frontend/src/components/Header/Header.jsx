import { useState } from "react";
import "./Header.scss";
import Rating from "./Rating/Rating";

export default function Header() {
	const ratingsData = [
		{ image: "/img/icons/bronza.svg", name: "Бронза" },
		{ image: "/img/icons/silver.svg", name: "Серебро" },
		{ image: "/img/icons/gold.svg", name: "Золото" },
		{ image: "/img/icons/diamond.svg", name: "Алмаз" },
		{ image: "/img/icons/best.svg", name: "Джедай" },
	];

	const [active, setActive] = useState(0);

	return (
		<div className="block-1">
			<div className="block-1__delivery">20 заказов/неделя</div>
			<ul className="block-1__ratings">
				{ratingsData.map((rating, i) => {
					return (
						<Rating
							key={i}
							rating={{ ...rating }}
							active={active}
							setActive={setActive}
							index={i}
						/>
					);
				})}
			</ul>
		</div>
	);
}
