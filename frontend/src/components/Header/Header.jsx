import { useContext, useEffect, useState } from "react";
import { RankTitleContext } from "../../providers/RankTitleProvider";
import { getRanks } from "../../services/getRanks";
import "./Header.scss";
import Rating from "./Rating/Rating";

export default function Header() {
	const [ranks, setRanks] = useState([]);
	const [active, setActive] = useState(0);
	const { setRankTitle } = useContext(RankTitleContext);

	useEffect(() => {
		getRanks(setRanks);
	}, []);

	const currentRank = ranks[active];
	useEffect(() => {
		setRankTitle(currentRank ? currentRank.title : "Бронза");
	});
	const currentPrize = currentRank ? currentRank.prize : 0;
	const currentOrdersCount = currentRank ? currentRank.orders_count : 0;

	return (
		<>
			<div className="block-1">
				<div className="block-1__delivery">
					{currentOrdersCount} заказов/неделя
				</div>
				<ul className="block-1__ratings">
					{ranks.map((rank, i) => {
						return (
							<Rating
								key={rank.id}
								rank={{ ...rank }}
								active={active}
								setActive={setActive}
								index={i}
							/>
						);
					})}
				</ul>
			</div>
			<div className="content__prize">Приз - {currentPrize} ₽</div>
		</>
	);
}
