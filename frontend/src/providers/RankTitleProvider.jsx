import { createContext, useState } from "react";

export const RankTitleContext = createContext();

export default function RankTitleProvider({ children }) {
	const [rankTitle, setRankTitle] = useState("Бронза");

	return (
		<RankTitleContext.Provider value={{ rankTitle, setRankTitle }}>
			{children}
		</RankTitleContext.Provider>
	);
}
