from django.db.models import QuerySet
from main.api.v1.schemas import SRank
from main.models import Rank


class RankService:
    @staticmethod
    def get_all() -> list[SRank]:
        """Возвращает все ранги."""
        ranks: QuerySet[Rank] = Rank.objects.all()
        return [
            SRank(
                id=rank.id,
                image=rank.image.url if rank.image else None,
                title=rank.title,
                prize=rank.prize,
                orders_count=rank.orders_count,
            )
            for rank in ranks
        ]

    @staticmethod
    def get_by_title(title: str) -> SRank:
        """Возвращает ранг по его названию."""
        rank: Rank | None = Rank.objects.filter(title=title).first()
        if rank is None:
            raise ValueError(f'Rank "{title}" not found')
        return rank
