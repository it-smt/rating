from django.conf import settings
from main.api.v1.schemas import SDriverShow
from main.models import People
from main.services.rank_service import RankService


class PeopleService:
    @staticmethod
    def get_by_rank(rank_name: str) -> list[SDriverShow]:
        """Получает водителей по рангу."""
        peoples: People = People.objects.filter(rank__title=rank_name).only(
            "name", "call_sign", "orders_count", "rank", "grade"
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

    @staticmethod
    def bulk_update_or_create(call_sign_counts: dict[str, int]) -> None:
        """Обновляет существующие записи или создает новые."""
        existing_people: dict[str, People] = {
            person.call_sign: person for person in People.objects.all()
        }

        to_update: list[People] = []
        to_create: list[People] = []

        rank = RankService.get_by_title(settings.BASE_RANK_TITLE)

        for call_sign, orders_count in call_sign_counts.items():
            if call_sign in existing_people:
                person: People = existing_people[call_sign]
                person.orders_count = orders_count
                to_update.append(person)
            else:
                to_create.append(
                    People(call_sign=call_sign, orders_count=orders_count, rank=rank)
                )

        if to_update:
            People.objects.bulk_update(to_update, fields=["orders_count"])

        if to_create:
            People.objects.bulk_create(to_create)
