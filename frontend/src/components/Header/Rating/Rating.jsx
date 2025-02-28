import "./Rating.scss";

export default function Rating({ active, setActive, rank, index }) {
	const handleClick = () => {
		setActive(index);
	};

	return (
		<li
			className={
				active == index ? "block-1__rating _active" : "block-1__rating"
			}
			id="ratingBlock"
			onClick={handleClick}
		>
			<img src={`http://212.67.13.120:8000${rank.image}`} alt="" />
			<span>{rank.title}</span>
		</li>
	);
}
