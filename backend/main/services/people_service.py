from main.api.v1.schemas import SDriverShow
from main.models import People


class PeopleService:
    @staticmethod
    def get_by_rank(rank_name: str) -> list[SDriverShow]:
        """Получает водителей по рангу."""
        peoples: People = People.objects.filter(rank__title=rank_name).only(
            "name", "call_sign", "orders_count", "rank__title", "grade"
        )
        return [
            SDriverShow(
                id=people.id,
                name=people.name,
                call_sign=people.call_sign,
                orders_count=people.orders_count,
                rank=people.rank.title,
                grade=people.grade,
            )
            for people in peoples
        ]
