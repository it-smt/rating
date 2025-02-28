import { createContext, useState } from "react";

export const DriversContext = createContext();

export default function DriversProvider({ children }) {
	const [drivers, setDrivers] = useState([]);

	return (
		<DriversContext.Provider value={{ drivers, setDrivers }}>
			{children}
		</DriversContext.Provider>
	);
}
