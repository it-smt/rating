import Drivers from "./components/Drivers/Drivers";
import Header from "./components/Header/Header";
import DriversProvider from "./providers/DriversProvider";
import RankTitleProvider from "./providers/RankTitleProvider";
import "./scss/base.style.scss";
import "./scss/index.style.scss";
import "./scss/null.style.scss";

export default function App() {
	return (
		<div className="wrapper">
			<div className="container">
				<main className="content">
					<DriversProvider>
						<RankTitleProvider>
							<Header />
							<Drivers />
						</RankTitleProvider>
					</DriversProvider>
				</main>
			</div>
		</div>
	);
}
