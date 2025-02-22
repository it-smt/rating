from main.api.v1.schemas import SDriverShow
from main.models import People


class PeopleService:
    @staticmethod
    def get_by_rank(rank_name: str) -> list[SDriverShow]:
        """Получает водителей по рангу."""
        peoples: People = People.objects.filter(rank__title=rank_name).values(
            "name", "call_sign", "orders_count", "rank__title", "grade"
        )
        return [SDriverShow(*people) for people in peoples]
