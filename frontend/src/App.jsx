import Drivers from "./components/Drivers/Drivers";
import Header from "./components/Header/Header";
import "./scss/base.style.scss";
import "./scss/index.style.scss";
import "./scss/null.style.scss";

export default function App() {
	return (
		<div className="wrapper">
			<div className="container">
				<main className="content">
					<Header />
					<div className="content__prize">Приз - 0 ₽</div>
					<Drivers />
				</main>
			</div>
		</div>
	);
}
