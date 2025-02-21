import "./Rating.scss";

export default function Rating({ active, setActive, rating, index }) {
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
			<img src={rating.image} alt="" />
			<span>{rating.name}</span>
		</li>
	);
}
