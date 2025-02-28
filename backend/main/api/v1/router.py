from django.http import HttpRequest
from ninja import Router

from main.services.rank_service import RankService
from main.api.v1.schemas import SDriverShow, SMsg, SRank
from main.services.people_service import PeopleService

router = Router()


@router.get("drivers/", response={200: list[SDriverShow], 400: SMsg})
def get_drivers(request: HttpRequest, rank_name: str = "Бронза") -> list[SDriverShow]:
    """Получение всех водителей."""
    return PeopleService.get_by_rank(rank_name)


@router.get("ranks/", response={200: list[SRank], 400: SMsg})
def get_all_ranks(request: HttpRequest) -> list[SRank]:
    """Получение всех рангов."""
    return RankService.get_all()
